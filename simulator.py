from collections import defaultdict
import pandas as pd
from tqdm import tqdm


# Do not edit this code. Your submissions will anyway be executed against this exact simulator.


class Simulator(object):
    def __init__(self, model):
        self.model = model
        self.price_volume_data = pd.read_pickle('data/simulator_data.pickle')
        if not isinstance(model.required_rows, int):
            raise ValueError(f"Invalid required_rows parameter: {model.required_rows}")
        self.rows_to_feed_to_model = model.required_rows
        self.percentage_exchange_volume = 0.03
        self.fee_in_bips = 4.0
        self.position_limit = 200

        self.simulation_data = defaultdict(list)

    def run(self, start_date, end_date):
        try:
            start_index = self.price_volume_data.index.get_loc(start_date)
            end_index = self.price_volume_data.index.get_loc(end_date)
        except KeyError as e:
            raise ValueError("Date range does not fall within the supported range 01-01-2018 - 31-03-2022!") from e

        for i in tqdm(range(start_index, end_index)):
            timestamp = self.price_volume_data.index[i]
            current_data = self.price_volume_data.iloc[(i - self.rows_to_feed_to_model): i]
            current_position = 0.0 if not self.simulation_data else self.simulation_data['position'][-1]  # 0.0 if first
            current_price = self.price_volume_data.iloc[i]['price']
            current_volume = self.price_volume_data.iloc[i]['volume']

            target_position = self.model.compute_target_position(current_data, current_position)

            if target_position is None:
                continue

            self.execute_order(target_position, timestamp, current_volume, current_price, current_position)

    def execute_order(self, target_position, timestamp, current_volume, current_price, current_position):

        # Force target position within bounds
        target_position = max(-self.position_limit, target_position)
        target_position = min(self.position_limit, target_position)

        current_usd_cash = 0.0 if not (x := self.simulation_data['cash']) else x[-1]

        max_available_volume = self.percentage_exchange_volume * current_volume

        volume_matched = min(max_available_volume, abs(target_position - current_position))

        direction = 1.0 if target_position > current_position else -1.0
        new_position = current_position + direction * volume_matched

        transaction_cost_in_cash = direction * volume_matched * current_price
        fee = abs(transaction_cost_in_cash) * 0.0001 * self.fee_in_bips
        new_usd_cash = current_usd_cash - transaction_cost_in_cash - fee

        self.simulation_data['position'].append(new_position)
        self.simulation_data['cash'].append(new_usd_cash)
        self.simulation_data['timestamp'].append(timestamp)
        self.simulation_data['fee'].append(fee)
        self.simulation_data['profit'].append(new_usd_cash + new_position * current_price)

    def get_result_dataframe(self):
        if not self.simulation_data:
            columns = ['timestamp', 'position', 'cash', 'fee', 'profit',
                       'cumulative_fees', 'cumulative_fees', 'profit_without_fees']
            return pd.DataFrame(columns=columns)
        df = pd.DataFrame(self.simulation_data).set_index('timestamp')
        df['cumulative_fees'] = df['fee'].cumsum()
        df['profit_without_fees'] = df['profit'] + df['cumulative_fees']
        return df

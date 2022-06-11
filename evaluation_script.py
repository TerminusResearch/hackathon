import datetime

from simulator import Simulator
from strategy import MeanReversionStrategy
from strategy import YourStrategy
from util import call_with_timeout

# Do not edit this code!
# This is to show how precisely your code will be evaluated. The values of start_date and end_date may change.
# The data fed internally to the simulator may (and will) be extended by more recent data points.
# The train_data.pickle file WILL NOT CHANGE.

if __name__ == "__main__":
    # This call will possibly execute also your model training. Please, do not submit pretrained models.
    model = call_with_timeout(YourStrategy, 90*60)
    simulator = Simulator(model)

    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2022, 3, 30)

    call_with_timeout(simulator.run, 120*60, [start_date, end_date])

    df = simulator.get_result_dataframe()
    df.to_csv("sim_result.csv")

    profit = df['profit'][-1] if not df.empty else 0

    print("Results saved to sim_result.csv")
    print(f"Profit of the simulation: {profit}")

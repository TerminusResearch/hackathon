# Terminus Research Hackathon

## How to run the code

### Prerequisites
- [Install Poetry](https://python-poetry.org/docs/).
- [Install Python 3.9](https://www.google.com/search?q=How+do+I+install+Python+3.9&sxsrf=ALiCzsbJ0uvEleEjew7tXj4zIA0GpmPsdQ%3A1653952213025&ei=1U6VYvCXAeSMrwShq43wDA&ved=0ahUKEwiw1oeRrIj4AhVkxosKHaFVA84Q4dUDCA4&uact=5&oq=How+do+I+install+Python+3.9&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFkoECEEYAEoECEYYAFAAWABgkQZoAHAAeACAAZIBiAGSAZIBAzAuMZgBAKABAqABAcABAQ&sclient=gws-wiz)

### Installation

Run the following in your shell after downloading the code and unzipping
```
cd hackathon
poetry install
```

For executing the jupyter notebook `playground.ipynb` run

```
poetry run jupyter notebook
```

For executing for the evaluation script run

```
poetry shell
python evaluation_script.py
```

## The task

Implement a trading strategy for a (secretly constructed) TRCoin given its historical data. This typically has two components:

- Forecasting a suitable future price.
- Efficiently turning the price forecasts into positions.

For details of the trading behaviour, read carefully through `simulator.py`.

See also the example strategy in `strategy.py`.

### Data

- Training data covers the period from 2018-01-01 to 2022-01-01
- The simulator can run strategies on any date range in between 2018-01-01 and 2022-03-31
- The final evaluation will be performed by executing submitted code on the data in the range from 2022-04-01 to 2022-07-01

### A few tips

- The simulator can be executed also for earlier periods for more careful validation of your strategies.
- Positions held can also be negative.
- Strategies that hold large positions for long periods of time are typically not good trading strategies (e.g. naive HOLDing) and tend to generalize poorly. High frequency of position changes is a good (but not sufficient) indicator. Inspect the corresponding chart regularly (see `playgroung.ipynb`)
- Think twice about running expensive parameter tuning algorithms as it might be very easy to overfit to the short validation period.

## Submission

- Archive contains 2 files (strategy.py, pyproject.toml). Replace class YourStrategy(Strategy) in strategy.py by your strategy.
- There is a limit for submission per day (12)
- Profit calculation can take up to 15 minutes after submission, during this period score will be equal to '-1'
- There is limitation of submission archive size = 50Mb.

## Evaluation

The key metric is `profit` at the end of the trading window (see for example `evaluation_script.py`). This will determine the winner of the hackathon assuming no irregularities (access to external data, tampering with the simulator etc.) in the submitted code are found.

For the purposes of hiring to Terminus Research, we will pay much greater attention to the inventiveness, technical quality of implementation, and overall robustness of the strategy. Feel free to submit additional models you developed as well. If your strategy looks great to us but got "unlucky" in the testing period, we will contact you!

The reviews will be performed by our employees who are world-class experts in algorithmic trading as well as in modern machine learning.

### Intermediate leaderboard

During the competition, we will maintain a leaderboard corresponding to performance in between 2022-01-01 to 2022-04-01 (as specified in `evaluation_script.py`). This should give a general idea of the performance of the strategy. However, beware that your strategy might be overfit to the particular time period. In that sense, the leaderboard **will not be predictive** of the final test performance.

For this purpose, submit the `sim_result.csv` file (the output of `evaluation_script.py`). We will trust the fairness of your submission. However, our inability to reproduce the result once the code is submitted will lead to immediate disqualification.   )

### Final evaluation

For final evaluation, we will require the submission of source code. In particular,

- An updated `pyproject.toml` file that allows installation of specific python libraries you will require for your strategy.
- Your implementation of `strategy.py`
- Optionally a directory called `tools` which containts additional python scripts needed in `strategy.py`.

On the other hand, do NOT submit:

- any of the remaining python files (e.g. `simulator.py` or `evaluation_script.py`), we will provide them in their original form.
- any jupyter notebooks
- any files with data (again, they will be provided)
- any files containing trained ML models. Training should be included in the execution of `evaluation_script.py`.

The evaluation will proceed as follows:

- The data files will be extended to contain newer data points (both for training and for simulation).
- The simulation period will be adjusted in `evaluation_script.py`.
- The submitted files will be copied in the directory with the original hackathon code (overwriting the original files)
- The following will be executed:

There will be a limit of 90 minutes on training and 2 hours on the evaluation of the simulator, on a computer with 32GB RAM.

```
cd TR_hackathon
poetry install
poetry shell
python evaluation_script.py
```

Please guarantee success of the procedure by preparing your submission correctly. **Disfunctional submissions will not be evaluated**.

Good luck!



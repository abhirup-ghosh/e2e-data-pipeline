# Dataset: Football Data from Transfermarkt

Source: https://www.kaggle.com/datasets/davidcariboo/player-scores

## Download data 

### 1. Direct download

Download and unzip the `archive.zip` file and move it's contents to `data/` directory.

### Using kaggle api

Using Kaggle's public API to download the dataset [follow the documentation [here](https://www.kaggle.com/docs/api)].

1. Download Kaggle API (Check [reproducibility.md](../notes/reproducibility.md) for instructions regarding building conda environment `e2e-data-pipeline`)

```bash
conda activate e2e-data-pipeline
conda install conda-forge::kaggle -y
```

2. Authenticate [(instructions)](https://www.kaggle.com/docs/api#authentication) by creating an API token and storing it under `${HOME}/.kaggle/kaggle.json` on the VM.

3. Download dataset `davidcariboo/player-scores` inside `data/` directory and unzipping file.

```bash
kaggle datasets download -d davidcariboo/player-scores
unzip player-scores.zip 
rm player-scores.zip
```

## All Data

Either method generates the following raw data files:

```bash
data/
├── appearances.csv
├── club_games.csv
├── clubs.csv
├── competitions.csv
├── game_events.csv
├── game_lineups.csv
├── games.csv
├── player_valuations.csv
└── players.csv
```

## Tracking large files using `git lfs`

```bash
sudo apt-get install git-lfs
```
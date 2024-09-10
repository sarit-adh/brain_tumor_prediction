### Usage

Download data from kaggle

```bash
python download_data_from_kaggle.py
```


Train the model

```bash
python main.py --task train --epochs 20 --model vgg16
```

Load the trained model

```bash
python main.py --task load
```

### Command-Line Arguments

| Argument      | Type   | Default               | Description                                                                                                                                  |
|---------------|--------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `--model`     | `str`  | `"vgg16"`             | Base model name (options are vgg16, vgg19)                                                                                                   |
| `--epochs`    | `int`  | `10`                  | Number of epochs for training                                                                                                                |
| `--task`      | `str`  | `"load"`              | Task to perform. Options are: `train` to train the model and save the trained model, or `load` to load the saved model and perform evaluation|
| `--data_dir`  | `str`  | `"../data/raw/"`      | Folder to load the data from. Default is `../data/raw/`                                                                                      |
| `--model_dir` | `str`  | `"../trained_models/"`| Folder to save or load the model. The default directory is `../trained_models/`.                                                             |
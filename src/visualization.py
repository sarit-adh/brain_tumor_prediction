

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compare_model_classifications(report_dict, title):
    
    # Data preparation
    metrics = ['precision', 'recall', 'f1-score']  
    class_labels = sorted(list(report_dict.values())[0].keys())[:-3]

    # Initialize a list to hold data for DataFrame
    data = []

    #Fill up the data from classification report to data list
    for model_name, report in report_dict.items():
        for class_label in class_labels:
            for metric in metrics:
                row = {'Model': model_name, 'Class': class_label, 'Metric': metric, 'Score': report[class_label][metric]}
                data.append(row)

    # Convert the list to a DataFrame
    df = pd.DataFrame(data)

    # Plotting
    g = sns.catplot( x='Class', y='Score', hue='Model', col='Metric', data=df, kind='bar', height=3, aspect=1.5, legend_out=False)

    # Access the legend and set its location (e.g., 'upper right', 'lower left', 'center', etc.)
    for ax in g.axes.flat:
        ax.legend(loc='upper right')  # Set desired location here
        
    g.figure.suptitle(title, fontsize=12)
        
    plt.tight_layout()
    plt.show()
    
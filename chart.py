import sys, pypistats, datetime, matplotlib, argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
\
def main(package_name, cumulative=False, output_file='chart.svg'):
    # Fetch download statistics using pypistats
    data = pypistats.overall(package_name, total=True, format='pandas')
    data = data.query("category == 'without_mirrors'").sort_values("date")
    
    # Extract dates and download counts from the DataFrame
    dates = pd.to_datetime(data['date'])
    counts = data['downloads']

    # Calculate the total downloads and cumulative counts if needed
    total_downloads = counts.sum()
    if cumulative:
        counts = counts.cumsum()

    # Enable xkcd style with a standard font
    with plt.xkcd():
        matplotlib.rcParams['font.family'] = ['DejaVu Sans']
        # Create chart
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(dates, counts, marker='o', linestyle='-')
        ax.set_title(f"Downloads for '{package_name}'\n Total Downloads: {total_downloads}", fontsize=16)
        ax.set_xlabel('Date')
        ax.set_ylabel('Downloads')

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        plt.xticks(rotation=45)
        # Add gridlines
        ax.grid(True, linestyle='--', linewidth=0.5)
        plt.tight_layout()
        # Save the plot as an SVG file with bbox_inches='tight'
        plt.savefig(f'/output/{output_file}.svg', format='svg', bbox_inches='tight')

def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a PyPI download chart.')
    parser.add_argument('package_name', type=str, help='The name of the PyPI package.')
    parser.add_argument('--cumulative', type=str2bool, nargs='?', const=True, default=False, help='Generate a cumulative download chart.')
    parser.add_argument('--output_file', type=str, default='chart', help='The name of the output SVG file.')

    args = parser.parse_args()

    main(args.package_name, args.cumulative, args.output_file)
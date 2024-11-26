import sys
import pypistats
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import matplotlib

def main(package_name, cumulative=False):
    # Fetch download statistics using pypistats
    data = pypistats.overall(package_name,total = True, format = 'pandas')
    #print(data)
    data = data.groupby("category").get_group("without_mirrors").sort_values("date")
    
    # Extract dates and download counts from the DataFrame
    dates = pd.to_datetime(data['date'])
    counts = data['downloads']

    # Calculate the total downloads
    total_downloads = counts.sum()

    # If cumulative is True, compute the cumulative sum of downloads
    if cumulative:
        counts = counts.cumsum()

    # Enable xkcd style with a standard font
    with plt.xkcd():
        matplotlib.rcParams['font.family'] = ['DejaVu Sans']
        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(dates, counts, marker='o', linestyle='-')

        # Set title and labels
        ax.set_title(f"Downloads for '{package_name}'\n Total Downloads: {total_downloads}", fontsize=16)
        ax.set_xlabel('Date')
        ax.set_ylabel('Downloads')

        # Format the date axis
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        plt.xticks(rotation=45)
        # Add gridlines
        ax.grid(True, linestyle='--', linewidth=0.5)
        plt.tight_layout()
        # Save the plot as an SVG file with bbox_inches='tight'
        plt.savefig('/output/chart.svg', format='svg', bbox_inches='tight')

if __name__ == '__main__':
    package_name = sys.argv[1]
    # Check for optional cumulative argument
    cumulative = True if (len(sys.argv) > 2 and sys.argv[2].lower()=='cumulative') else False
        
    main(package_name, cumulative)
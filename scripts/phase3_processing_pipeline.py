import pandas as pd

file_list = [
    "../raw_data/jbm1 16-20.csv",
    "../raw_data/jbm2 16-20.csv"
]

output_file = "../output/cleaned_brts.csv"

chunk_size = 50000

first_chunk = True

for file in file_list:

    print("Processing:", file)

    for chunk in pd.read_csv(file, chunksize=chunk_size):

        # Convert time
        chunk['GPSTime'] = pd.to_datetime(chunk['GPSTime'], errors='coerce')
        chunk['InsertTime'] = pd.to_datetime(chunk['InsertTime'], errors='coerce')
        chunk['UpdatedTime'] = pd.to_datetime(chunk['UpdatedTime'], errors='coerce')

        # Generate Location from GPS
        chunk['Lat_round'] = chunk['Latitude'].round(3)
        chunk['Long_round'] = chunk['Longitude'].round(3)

        chunk['Location'] = (
            chunk['Lat_round'].astype(str)
            + "_"
            + chunk['Long_round'].astype(str)
        )

        # Remove helper columns
        chunk = chunk.drop(['Lat_round','Long_round'], axis=1)

        # Save chunk
        if first_chunk:
            chunk.to_csv(output_file, index=False)
            first_chunk = False
        else:
            chunk.to_csv(output_file, mode='a', header=False, index=False)

        print("Chunk processed")

print("Phase 3 processing complete")
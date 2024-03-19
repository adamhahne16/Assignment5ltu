# Assignment5ltu
This was a project in the course Industrial AI and eMaintenance.
The Assignment is done for task 1 for first grade. 
I got two datasets.
Point cloud data is stored as a 2D matrix
each row has 3 values i.e. the x, y, z value for a point. 

Task 1 Results after code execute: 
Processing dataset1, shape: (72067, 3)
Estimated ground level for dataset1: 61.15373000000003
Processing dataset2, shape: (84588, 3)
Estimated ground level for dataset2: 61.16522

Beyond the results above is the 2 histogram plots you can see the folder. 

Okey so the objective of Task 1 was to estimate the ground level from two point datasets. This was achieved by analyzing the distribution of the Z-values ("vertical axis") using a histogram. The peak of the histogram, representing the most frequently occurring Z-value, so the most "estimated" ground level. This method is based on the assumption that the most common elevation in a terrestrial point cloud dataset corresponds to the ground. So like the most common height in a ground-based point cloud dataset corresponds to the ground.

And after processing the datasets, the estimated ground levels were determined to be around 61.15 for dataset1 and 61.17 for dataset2. These values indicate the most common elevations within each dataset, the ground levels are relatively consistent. The histograms is saved within the project folder. visually we saw a clear peak at the estimated ground levels for both datasets.





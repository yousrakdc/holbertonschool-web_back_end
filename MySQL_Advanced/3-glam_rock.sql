-- Lists all bands with Glam rock as their main style, ranked by their longevity
-- Column names: band_name and lifespan (in years until 2024)
-- Uses attributes formed and split for computing the lifespan

SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
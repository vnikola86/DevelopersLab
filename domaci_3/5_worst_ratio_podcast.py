def worst_ratio_podcast(podcasts):
    worst_ratio = float('inf')
    worst_podcast = None

    for podcast in podcasts:
        positive_comments = podcast['br_pozitivni']
        negative_comments = podcast['br_negativni']
        
        if negative_comments != 0:
            ratio = positive_comments / negative_comments
        else:
            ratio = positive_comments + 0.5
        
        if ratio < worst_ratio:
            worst_ratio = ratio
            worst_podcast = podcast['naziv']

    return worst_podcast

# Test the function
podcasts = [
    {'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10},
    {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30},
    {'naziv': 'Science VS.', 'br_pozitivni': 600, 'br_negativni': 45}
]

worst_podcast = worst_ratio_podcast(podcasts)
print("Worst ratio podcast:", worst_podcast)

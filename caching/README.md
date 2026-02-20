# Caching System

This directory contains several Python modules that implement different caching algorithms. Each cache class inherits from a common base class and demonstrates a specific cache replacement policy. These are useful for understanding and experimenting with cache management strategies.

## Files and Classes

- **base_caching.py**: Defines the `BaseCaching` class, which provides the basic structure for all cache classes, including a dictionary for storing cache data and a constant `MAX_ITEMS` (set to 4).

- **0-basic_cache.py**: Implements `BasicCache`, a simple cache with no eviction policy. Items are added and retrieved, but if the cache exceeds `MAX_ITEMS`, no items are discarded automatically.

- **1-fifo_cache.py**: Implements `FIFOCache`, which uses the First-In-First-Out (FIFO) eviction policy. When the cache exceeds `MAX_ITEMS`, the oldest item is removed.

- **2-lifo_cache.py**: Implements `LIFOCache`, which uses the Last-In-First-Out (LIFO) eviction policy. When the cache exceeds `MAX_ITEMS`, the most recently added item is removed.

- **3-lru_cache.py**: Implements `LRUCache`, which uses the Least Recently Used (LRU) eviction policy. When the cache exceeds `MAX_ITEMS`, the least recently accessed item is removed.

- **4-mru_cache.py**: Implements `MRUCache`, which uses the Most Recently Used (MRU) eviction policy. When the cache exceeds `MAX_ITEMS`, the most recently accessed item is removed.

## Usage

Each cache class provides `put(key, item)` and `get(key)` methods. You can instantiate any cache class and use these methods to store and retrieve items according to the class's eviction policy.

## Example

```python
from 1-fifo_cache import FIFOCache

cache = FIFOCache()
cache.put('A', 'Apple')
cache.put('B', 'Banana')
cache.put('C', 'Cherry')
cache.put('D', 'Date')
cache.put('E', 'Elderberry')  # This will evict 'A' (FIFO)

print(cache.get('A'))  # None
print(cache.get('B'))  # 'Banana'
```

## License

This project is for educational purposes.

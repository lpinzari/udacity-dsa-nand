# HTTP Router using Trie

The basic idea is to implement a HTTP Router with response handlers in the form of strings. The key data structure is a **Trie**, whose nodes store a part of the url (*i.e* http path) and a string to ensure we got the right handler for the http request.

For instance, a Trie with a single path entry of: `"/home/about/me"` would look like this:

(root, None) -> ("home", None) -> ('about', None) -> ("me", "about me handler")

The operations to be implemented in a HTTP Router interface are:

- `add_handler(url_path, handler)`
- `lookup(url_path)`

The program uses three classes: **Router, RouteTrie** and **RouteTrieNode**. The Router class wraps the RouteTrie and provides the public methods of the HTTP Router interface.

## Time and Space Complexity

The **Time and Space Complexity** of the Router class method `add_handler` is **O(n)**, where **n** is the number of parts in the url path.

As for the **Time Complexity**, the function calls the `split_path(url_path)` method to split the path around the '/' character and returning a list of **path_parts**. The time complexity of this function is **O(n)**. Lastly, the insert function loops through a list of strings inserting the string into the Trie where nedded. The `insert` method has **O(n)** time complexity, resulting in an overall time complexity of **O(n)**. Similarly, the **Space Complexity** depends on the number of nodes in the Trie and, hence, it scales proportionally to the number of parts in the url_path.

The same reasoning can be extended to the `lookup` method. 

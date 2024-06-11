# Static Site Generator

A static site generator takes raw content files (like Markdown and images) and turns them into a static website of HTML and CSS files.

### Headings

```
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
```
```
# Heading 1

## Heading 2

### Heading 3
```

### Paragraphs

```
<p>This is a paragraph of text.</p>
```
```
This is a paragraph of text.
```

### Bold

```
<p>This is a <b>bold</b> word.</p>
```
```
This is a **bold** word.
```

### Italics

```
<p>This is an <i>italic</i> word.</p>
```
```
This is an *italic* word.
```

### Links

```
This is a paragraph with a <a href="https://www.google.com">link</a>.
```
```
This is a paragraph with a [link](https://www.google.com).
```

### Rendering images

```
<img src="url/of/image.jpg" alt="Description of image">
```
```
![alt text for image](url/of/image.jpg)
```

### Unordered lists

```
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```
```
* Item 1
* Item 2
* Item 3
```

### Ordered lists

```
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```
```
1. Item 1
2. Item 2
3. Item 3
```

### Quotes

```
<blockquote>
    This is a quote.
</blockquote>
```
```
> This is a quote.
```

### Code

```
<code>This is code</code>
```
````
```
This is code
```
````

## Run

``` main.sh ``` generates a website and starts a simple web server \
``` test.sh ``` runs tests

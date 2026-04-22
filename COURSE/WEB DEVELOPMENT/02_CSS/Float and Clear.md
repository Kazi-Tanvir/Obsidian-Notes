---
tags:
- css
- layout
- legacy
---
# Float and Clear

## What's the Actual Use?
Originally used for wrapping text around images, `float` was historically used for full-page layouts before Flexbox and Grid. `clear` is used to stop elements from floating next to each other.

## Other Common Use Cases
- Wrapping text around a pull-quote or image in a blog post.
- Maintenance on older legacy websites.

## Documentation & Code
- `float`: `left`, `right`, or `none`.
- `clear`: `left`, `right`, `both`.

````css
.image-left {
    float: left;
    margin-right: 15px;
}

/* Clearfix to prevent parent collapse */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
````

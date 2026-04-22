---
tags:
- html
- media
- lists
- tables
---
# Images, Lists, and Tables

## What's the Actual Use?
These elements allow you to display visual content and organize data either sequentially (lists) or in a grid format (tables).

## Other Common Use Cases
- Creating navigation menus using `<ul>` and `<li>`.
- Displaying product specifications or pricing plans using `<table>`.

## Documentation & Code
- `<img>`: Self-closing tag for images; needs `src` and `alt`.
- `<ul>`/`<ol>`: Unordered (bullets) and Ordered (numbers) lists.
- `<table>`: Uses `<tr>` (rows), `<th>` (headers), and `<td>` (data).

````html
<!-- Image -->
<img src="logo.png" alt="Company Logo" width="200">

<!-- Lists -->
<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>

<!-- Table -->
<table>
    <tr>
        <th>Topic</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>HTML Basics</td>
        <td>Completed</td>
    </tr>
</table>
````

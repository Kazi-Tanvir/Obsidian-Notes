---
title: "PRAC GUI 06 - red bmp"
aliases:
  - red bmp
  - 06_red_bmp
tags:
  - type/practice
  - c/bmp-format
  - c/binary-io
  - c/structs
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/image_editor/gui/06_red_bmp.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 29 - grayscale]]"
created: 2026-10-29
status: draft
---
# PRAC GUI 06 - red bmp

> [!abstract] Summary
> Generates an uncompressed 24-bit pure red BMP image from scratch by writing binary headers and raw BGR byte triples.

**Source:** `PRACTICE/image_editor/gui/06_red_bmp.c`

## Problem
Implement `red bmp` as part of the step-by-step image processing tutorial series, demonstrating binary BMP manipulation and pixel math.

## Concepts used
- **Packed BMP Structs:** Direct binary mapping of `BMPHeader` and `BMPInfoHeader`.
- **Pixel Manipulation:** Reading and modifying raw 24-bit BGR color bytes.
- **File Serialization:** Streaming processed pixel buffers back to disk in standard Windows BMP format.

## Code
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma pack(push, 1)
typedef struct {
    unsigned short bfType;
    unsigned int   bfSize;
    unsigned short bfReserved1;
    unsigned short bfReserved2;
    unsigned int   bfOffBits;
} BMPFileHeader;

typedef struct {
    unsigned int   biSize;
    int            biWidth;
    int            biHeight;
    unsigned short biPlanes;
    unsigned short biBitCount;
    unsigned int   biCompression;
    unsigned int   biSizeImage;
    int            biXPelsPerMeter;
    int            biYPelsPerMeter;
    unsigned int   biClrUsed;
    unsigned int   biClrImportant;
} BMPInfoHeader;
#pragma pack(pop)

typedef struct {
    unsigned char r;
    unsigned char g;
    unsigned char b;
} Pixel;

typedef struct {
    int width;
    int height;
    Pixel *data;
} Image;

Image *create_image(int width, int height) {
    if (width <= 0 || height <= 0) return NULL;
    Image *img = (Image *)malloc(sizeof(Image));
    if (!img) return NULL;

    img->width  = width;
    img->height = height;
    img->data   = (Pixel *)calloc((size_t)width * height, sizeof(Pixel));
    if (!img->data) {
        free(img);
        return NULL;
    }
    return img;
}

void free_image(Image *img) {
    if (!img) return;
    if (img->data) {
        free(img->data);
        img->data = NULL;
    }
    free(img);
}

int save_bmp(const char *filename, const Image *img) {
    if (!img || !img->data || !filename) return 0;

    FILE *file = fopen(filename, "wb");
    if (!file) return 0;

    int width = img->width;
    int height = img->height;
    int padding = (4 - ((width * 3) % 4)) % 4;
    int row_size = width * 3 + padding;
    int data_size = row_size * height;

    BMPFileHeader header;
    header.bfType = 0x4D42;
    header.bfSize = sizeof(BMPFileHeader) + sizeof(BMPInfoHeader) + data_size;
    header.bfReserved1 = 0;
    header.bfReserved2 = 0;
    header.bfOffBits = sizeof(BMPFileHeader) + sizeof(BMPInfoHeader);

    BMPInfoHeader info_header;
    memset(&info_header, 0, sizeof(BMPInfoHeader));
    info_header.biSize = sizeof(BMPInfoHeader);
    info_header.biWidth = width;
    info_header.biHeight = height;
    info_header.biPlanes = 1;
    info_header.biBitCount = 24;
    info_header.biCompression = 0;
    info_header.biSizeImage = data_size;

    fwrite(&header, sizeof(BMPFileHeader), 1, file);
    fwrite(&info_header, sizeof(BMPInfoHeader), 1, file);

    unsigned char pad[3] = {0, 0, 0};

    for (int y = height - 1; y >= 0; y--) {
        for (int x = 0; x < width; x++) {
            int idx = y * width + x;
            unsigned char bgr[3] = {
                img->data[idx].b,
                img->data[idx].g,
                img->data[idx].r
            };
            fwrite(bgr, 1, 3, file);
        }
        if (padding > 0) {
            fwrite(pad, 1, padding, file);
        }
    }

    fclose(file);
    return 1;
}

int main(void) {
    int width = 200;
    int height = 200;

    Image *img = create_image(width, height);
    if (!img) {
        fprintf(stderr, "Failed to allocate memory.\n");
        return EXIT_FAILURE;
    }

    int total_pixels = width * height;
    for (int i = 0; i < total_pixels; i++) {
        img->data[i].r = 255;
        img->data[i].g = 0;
        img->data[i].b = 0;
    }

    if (save_bmp("red.bmp", img)) {
        printf("Saved: red.bmp (200x200 pixels)\n");
    } else {
        fprintf(stderr, "Failed to write red.bmp\n");
    }

    free_image(img);
    return EXIT_SUCCESS;
}
```

## How it works
1. Opens source image or prepares destination file stream in binary mode (`"rb"` / `"wb"`).
2. Reads or generates valid 14-byte file header and 40-byte info header.
3. Iterates over rows and columns, computing pixel transformations.
4. Handles padding and writes binary output to disk.

## Sample run
```text
(Generates or renders transformed BMP image: red bmp.bmp)
```

## Gotchas
> [!warning] BGR Channel Ordering
> Windows BMP files store color channels as Blue, Green, Red. Operating on channels assuming RGB ordering swaps colors unexpectedly.

## My notes
> [!question]- My notes

## Related
- [[LAB 29 - grayscale]]

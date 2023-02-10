## Math API Server

### Area Routes

#### Square

`/area/square`

![area-square](img/readme/area-square.png)



| Variable | Description |
| -------- | ----------- |
| s        | Side length |



#### Rectangle

`/area/rectangle` 

![area-rectangle](img/readme/area-rectangle.png)



| Variable           | Description         |
| ------------------ | ------------------- |
| l (lower case ell) | Length of rectangle |
| w                  | Width of rectangle  |



#### Triangle

`/area/triangle`

![area-triangle](img/readme/area-triangle.png)



| Variable | Description        |
| -------- | ------------------ |
| b        | Base of Triangle   |
| h        | Height of triangle |



#### Triangle - Heron's Formula

`/area/heron`

![heron](img/readme/heron.png)



| Variable | Description   |
| -------- | ------------- |
| a        | Side length a |
| b        | Side length b |
| c        | Side length c |

On this one, `s` is included in the returned JSON.



#### Parallelogram

`/area/parallelogram`

![area-parallelogram](img/readme/area-parallelogram.png)

| Variables | Description    |
| --------- | -------------- |
| b         | Base dimension |
| h | Height of parallelogram |





#### Circle

`/area/circle`

![area-circle](img/readme/area-circle.png)

Use `math.pi` instead of 3.14

| Variable | Notes                |
| -------- | -------------------- |
| r        | Radius of the circle |





#### Trapezoid

`/area/trapezoid`

![area-trapezoid](img/readme/area-trapezoid.png)



| Variables | Notes                   |
| --------- | ----------------------- |
| b1        | Length of one base      |
| b2        | Length of other base    |
| h         | Height of the trapezoid |



### Surface Area Routes

#### Cube

`/surface/cube`

![surface-cube](img/readme/surface-cube.png)

| Variable | Notes                   |
| -------- | ----------------------- |
| s        | Side length of the cube |



#### Sphere

`/surface/sphere`

![surface-sphere](img/readme/surface-sphere.png)


| Variable | Notes            |
| -------- | ---------------- |
| r        | Radius of sphere |



#### Cylinder

`/surface/cylinder`

![surface-cylinder](img/readme/surface-cylinder.png)

| Variables | Notes                  |
| --------- | ---------------------- |
| r         | Radius of the cylinder |
| h         | Height of the cylinder |





### Perimeter Routes 

#### Square

`/perimeter/square`

![perimeter-square](img/readme/perimeter-square.png)

| Variable | Notes                     |
| -------- | ------------------------- |
| s        | Side length of the square |





#### Rectangle

`/perimeter/rectangle`

![perimeter-rectangle](img/readme/perimeter-rectangle.png)

| Variables          | Notes                   |
| ------------------ | ----------------------- |
| l (lower case ell) | Length of the rectangle |
| w                  | Width of the rectangle  |



#### Triangle

`/perimeter/triangle`

![perimeter-triangle](img/readme/perimeter-triangle.png)

| Variable | Notes                   |
| -------- | ----------------------- |
| s1       | Side length of triangle |
| s2       | Side length of triangle |
| s3       | Side length of triangle |



#### Circle (Circumference)

`/perimeter/circle`

![perimeter-circle](img/readme/perimeter-circle.png)

| Variable | Notes           |
| -------- | --------------- |
| d        | Circle diameter |



### Volume Routes

#### Cube

`/volume/cube`

![vol-cube](img/readme/vol-cube.png)

| Variable | Notes       |
| -------- | ----------- |
| s        | side length |



#### Rectangular Prism

`/volume/prism`

![vol-rect](img/readme/vol-rect.png)

| Variable | Notes  |
| -------- | ------ |
| l        | Length |
| w        | Width  |
| h        | Height |



#### Square Pyramid

`/volume/pyramid`

![vol-squarepyramid](img/readme/vol-squarepyramid.png)

| Variable | Notes  |
| -------- | ------ |
| b        | Base   |
| h        | Height |





#### Cylinder

`/volume/cylinder`

![vol-cylinder](img/readme/vol-cylinder.png)

| Variable | Notes              |
| -------- | ------------------ |
| r        | Radius of circle   |
| h        | Height of cylinder |



#### Cone

`/volume/cone`

![vol-cone](img/readme/vol-cone.png)

| Variable | Notes              |
| -------- | ------------------ |
| r        | Radius of circle   |
| h        | Height of cylinder |

#### Sphere

`/volume/sphere`

![vol-sphere](img/readme/vol-sphere.png)

| Variable | Notes            |
| -------- | ---------------- |
| r        | Radius of sphere |



### Misc Routes

#### Distance Formula

`/distance`

![distance](img/readme/distance.png)

| Variable | Notes                    |
| -------- | ------------------------ |
| x1, y1   | Position of first point  |
| x2, y2   | Position of second point |





#### Slope

`/slope`

![lineslope](img/readme/lineslope.png)

| Variable | Notes                    |
| -------- | ------------------------ |
| x1, y1   | Position of first point  |
| x2, y2   | Position of second point |

#### Pythagorean Theorem

`/pythag`

![pythag](img/readme/pythag.png)


The JSON returned contains all 3 values.

For example calls to `/pythag?a=3&b=4`, `/pythag?b=4&c=5` & `/pythag?a=3&c=5` should all return the same JSON below. 

```json
{
    "a": 3,
    "b": 4,
    "c": 5
}
```



#### Mean

`/mean`

![mean](img/readme/mean.png)

Solve for the average of all numbers passed as a comma separated list. 

| Variable | Description                                                  |
| -------- | ------------------------------------------------------------ |
| nums     | A comma separated list of integers to average. For example, if you want to average the numbers 1, 2, & 3 the route would look like `/mean?nums=1,2,3` |

In the JSON returned, the values are returned as an array. For example, `/mean?nums=1,2,3` should return the following JSON.

```json
{
    "mean": 2,
    "nums": [
        1,
        2,
        3
    ]
}
```



#### Median

`/median`

Finds the median value, the value in the middle, of a comma separated list of integers.  If there are an odd number of values, it is the middle value. If there are an even number of values, it is the average of the middle two. 

| Variable | Description                      |
| -------- | -------------------------------- |
| nums     | Comma separate list of integers. |

Like the mean route, `nums` is included in the returned JSON as an array. 



#### Mode

`/mode`

Finds the mode - the most common - of a list of comma separated values. 

| Variable | Description                      |
| -------- | -------------------------------- |
| nums     | Comma separate list of integers. |

Like the mean route, `nums` is included in the returned JSON as an array. 

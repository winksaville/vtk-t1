# Vtk initial test

Following these instructions: https://docs.vtk.org/en/latest/getting_started/index.html#using-python

## Install

- Clone repo
  - `git clone git@github.com:winksaville/vtk-t1`
- Activate environment
  - `source ./env/bin/activate`

## Run

Cylinder example from: https://examples.vtk.org/site/Python/GeometricObjects/CylinderExample/
```bash
$ python CylinderExample.py
```

Test what happens when you call zoom before and after ResetCamera.

The first 4 work as camera.Zoom(z) is invoked after ResetCamera.
The next four fail because the ResetCamera resets zoom to 1.0,
thus the zoom angle is always 30 degrees.
```bash
$ python vtk-zoom-before-reset-fails.py 
works  z=1.50   eva=20.00  va=20.00 
works  z=0.75   eva=40.00  va=40.00 
works  z=0.25   eva=120.00 va=120.00
works  z=0.50   eva=60.00  va=60.00 
fails  z=1.50   eva=20.00  va=30.00 
fails  z=0.75   eva=40.00  va=30.00 
fails  z=0.25   eva=120.00 va=30.00 
fails  z=0.50   eva=60.00  va=30.00 
```

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.


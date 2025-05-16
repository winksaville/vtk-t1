#!/usr/bin/env python

# If you call camera.Zoom() it must be after ResetCamera() if you call it
# before ResetCamera() sets zoom to 1 and hence the view angle to 30 degrees.

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()
    # Set the background color.
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)

    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window. The render window interactor captures mouse events and will
    # perform appropriate camera or actor manipulation depending on the
    # nature of the events.
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    ren.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(400, 400)

    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()
    camera = ren.GetActiveCamera()

    def show(z, reset_first, expected_va):

        if reset_first:
            ren.ResetCamera()
        camera.Zoom(z)
        if not reset_first:
            ren.ResetCamera()

        va = camera.GetViewAngle()
        result = "works" if expected_va == va else "fails"
        msg = f'{result:<6} z={z:<6.2f} eva={expected_va:<6.2f} va={va:<6.2f}'
        print(msg)

        renWin.SetWindowName(msg)
        renWin.Render()
        iren.Start()

    show(1.5, True, 20)
    show(0.75, True, 40)
    show(0.25, True, 120)
    show(0.5, True, 60)

    show(1.5, False, 20)
    show(0.75, False, 40)
    show(0.25, False, 120)
    show(0.5, False, 60)

if __name__ == '__main__':
    main()

from engineering.fluid_mechanics import FluidMechanics


fluid = FluidMechanics()

print(fluid.density(1000, 1))

print(
    fluid.reynolds_number(
        1000,
        2,
        0.05,
        0.001
    )
)
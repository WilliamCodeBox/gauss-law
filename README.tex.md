# gauss-law

Gauss's law in Maxwell's Equations

> The total electric flux $\Psi$ through any closed surface is equal to the total charge enclosed by that surface

$$
\Psi = Q_{enc}
$$

Based on the definition of $\Psi$

$$
\Psi = \int_S \mathbf{D} \cdot d\mathbf{S}
$$

the total charge enclosed Q can be computed using the volume charge density $\rho_v$

$$
Q = \int_V \rho_v dv
$$

## The integral form of Gauss's law for electric field

$$
\int_S \mathbf{D} \cdot d\mathbf{S} = \int_V \rho_v dv
$$

## The differential form of Gauss's law for electirc field

Applying the divergence theorem to the definition of $\Psi$

$$
\Psi = \int_S \mathbf{D} \cdot d\mathbf{S} = \int_V \nabla \cdot \mathbf{D} dv
$$

Comparing with the integral form of Gauss's law, we can get its differential form

$$
\rho_v = \nabla \cdot \mathbf{D}
$$

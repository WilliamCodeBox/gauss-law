# gauss-law

Gauss's law in Maxwell's Equations

> The total electric flux <img src="/tex/535b15667b86f1b118010d4c218fecb9.svg?invert_in_darkmode&sanitize=true" align=middle width=12.785434199999989pt height=22.465723500000017pt/> through any closed surface is equal to the total charge enclosed by that surface

<p align="center"><img src="/tex/e34234683509423658280cac5a0dbee5.svg?invert_in_darkmode&sanitize=true" align=middle width=67.93608195pt height=14.42921205pt/></p>

Based on the definition of <img src="/tex/535b15667b86f1b118010d4c218fecb9.svg?invert_in_darkmode&sanitize=true" align=middle width=12.785434199999989pt height=22.465723500000017pt/>

<p align="center"><img src="/tex/7b94db5d05a6503ed868e2cfa3930e05.svg?invert_in_darkmode&sanitize=true" align=middle width=101.5258497pt height=37.3519608pt/></p>

the total charge enclosed Q can be computed using the volume charge density <img src="/tex/50d25a5a9015103272e88b9f86c3d050.svg?invert_in_darkmode&sanitize=true" align=middle width=15.48714584999999pt height=14.15524440000002pt/>

<p align="center"><img src="/tex/10dacb67c0ddfa4893946723e1d47e1a.svg?invert_in_darkmode&sanitize=true" align=middle width=91.6236189pt height=37.3519608pt/></p>

## Two forms of Gauss's law

### The integral form of Gauss's law for electric field

<p align="center"><img src="/tex/0b50aea868ca41545a85f119c180b5d9.svg?invert_in_darkmode&sanitize=true" align=middle width=145.45097984999998pt height=37.3519608pt/></p>

### The differential form of Gauss's law for electirc field

Applying the divergence theorem to the definition of <img src="/tex/535b15667b86f1b118010d4c218fecb9.svg?invert_in_darkmode&sanitize=true" align=middle width=12.785434199999989pt height=22.465723500000017pt/>

<p align="center"><img src="/tex/7f687ee6916c3bf2213238c78d2097f7.svg?invert_in_darkmode&sanitize=true" align=middle width=203.9132799pt height=37.3519608pt/></p>

Comparing with the integral form of Gauss's law, we can get its differential form

<p align="center"><img src="/tex/9e82efe446246d1331fae75dbd8a2fae.svg?invert_in_darkmode&sanitize=true" align=middle width=78.29498654999999pt height=14.4748956pt/></p>

## Applications of Gauss's law

Finding the vector fields, <img src="/tex/ae48dff45ab57dda34b441bc7904377a.svg?invert_in_darkmode&sanitize=true" align=middle width=12.420021899999991pt height=22.55708729999998pt/> or <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/>, by construting a proporate Gaussian surface.

> The ability to take <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> out of the integral sign

### Point Charge

![Point charge](./images/point-charge.png)

A point charge Q is located at the origin, to determine <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> at point P.

With Q given, all we have to do is constructing a _symmetry gaussian surface_, which makes the integral easy to solve.

<p align="center"><img src="/tex/77f808f871e294af1a0d109bbf496d89.svg?invert_in_darkmode&sanitize=true" align=middle width=263.14655565pt height=37.3519608pt/></p>

### Infinite Line Charge

![infinite-line-charge](./images/infinite-line-charge.png)

An infinite line of charge <img src="/tex/d1af9fdedbb7ff16eba3de01205aa337.svg?invert_in_darkmode&sanitize=true" align=middle width=17.51720849999999pt height=14.15524440000002pt/> lies along the z-axis, to determine <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> at point P.

First we have to determin the Q, in this problem, we can take a segement <img src="/tex/4c9c7ea8b81f7ac705c082f13bdb0b93.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=24.65753399999998pt/> of the infinite line.

For each element charge <img src="/tex/dba6dadac8da6ac22a875c766d176967.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> on segement <img src="/tex/4c9c7ea8b81f7ac705c082f13bdb0b93.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=24.65753399999998pt/>, it generates a <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> which can be separated into a z-component and a <img src="/tex/6dec54c48a0438a5fcde6053bdb9d712.svg?invert_in_darkmode&sanitize=true" align=middle width=8.49888434999999pt height=14.15524440000002pt/>-component. A cooresponding element charge <img src="/tex/ec2c3ba6e7093684cb5830f99fea40ad.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> exists, and the z-components of <img src="/tex/dba6dadac8da6ac22a875c766d176967.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> and <img src="/tex/ec2c3ba6e7093684cb5830f99fea40ad.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> cancels, resulting only <img src="/tex/6dec54c48a0438a5fcde6053bdb9d712.svg?invert_in_darkmode&sanitize=true" align=middle width=8.49888434999999pt height=14.15524440000002pt/>-components exist.

<p align="center"><img src="/tex/24adceabdd25bf476e70a067ca1c3655.svg?invert_in_darkmode&sanitize=true" align=middle width=314.64080835pt height=37.3519608pt/></p>

### Infinite Sheet of Charge

![infinite-sheet-charge](./images/infinite-sheet-charge.png)

An infinite sheet of uniform charge <img src="/tex/0f8f0e6d3382575ac9df9c33025eaf4d.svg?invert_in_darkmode&sanitize=true" align=middle width=17.19983594999999pt height=14.15524440000002pt/> lies con the xy-plane, to determine <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> at point P.

For each element charge <img src="/tex/dba6dadac8da6ac22a875c766d176967.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/>, it generates a <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/>, which can be separated into a z-component, a x-component, and a y-component. A coorespoding element charge <img src="/tex/ec2c3ba6e7093684cb5830f99fea40ad.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> exists. The x-components and y-components of <img src="/tex/dba6dadac8da6ac22a875c766d176967.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> and <img src="/tex/ec2c3ba6e7093684cb5830f99fea40ad.svg?invert_in_darkmode&sanitize=true" align=middle width=28.103935199999988pt height=22.831056599999986pt/> cancel each other, resulting only z-components exists.

<p align="center"><img src="/tex/820d16f732f5fc86b36a57c06b44bc44.svg?invert_in_darkmode&sanitize=true" align=middle width=544.7209416pt height=41.05060575pt/></p>

### Uniformly Charged Sphere

![uniform-charged-sphere](uniform-charged-sphere.png)

A sphere of radius <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> with a uniform charge <img src="/tex/2290e37f43b98d4ecfe494284e9af9f0.svg?invert_in_darkmode&sanitize=true" align=middle width=14.987486249999991pt height=14.15524440000002pt/>, to determine <img src="/tex/17104becada06c6cda0447c33ec6c846.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49764249999999pt height=22.55708729999998pt/> at point P.

For <img src="/tex/24a8624d29cb219184abc1d756669d70.svg?invert_in_darkmode&sanitize=true" align=middle width=38.47973909999999pt height=20.908638300000003pt/>

<p align="center"><img src="/tex/1441cb89f5b872f419881b7e0cf17311.svg?invert_in_darkmode&sanitize=true" align=middle width=260.61745215pt height=37.3519608pt/></p>

<p align="center"><img src="/tex/ffbd0a6d6d828f54b7b595ebe26e5cfd.svg?invert_in_darkmode&sanitize=true" align=middle width=228.75865484999997pt height=37.3519608pt/></p>

For <img src="/tex/08999c23f2c6c3e188bec1c4a51a9d79.svg?invert_in_darkmode&sanitize=true" align=middle width=38.47973909999999pt height=20.908638300000003pt/>

<p align="center"><img src="/tex/565a5d4ae2d67d40c514e9a0212f79b0.svg?invert_in_darkmode&sanitize=true" align=middle width=109.14811215pt height=32.990165999999995pt/></p>

<img src="/tex/535b15667b86f1b118010d4c218fecb9.svg?invert_in_darkmode&sanitize=true" align=middle width=12.785434199999989pt height=22.465723500000017pt/> stays the same.

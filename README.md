# Final_Project_SW_Engineering

In recent years, there has been a tremendous development in the field of Combinatorial Design Theory.
During this growth, new tools and new families of algorithms were developed. 
The aim of this project is to apply these new tools to a famous combinatorial problem that is fundamentally a problem of satisfying the 
constraints of permutation matrices.

A subgraph H of a given edge-colored graph is rainbow if the edge colors are all distinct. 
How many rainbow-perfect matchings are there in a given balanced bipartite properly colored graph? 

This is a #P-hard problem, and so it is unlikely that there exists an efficient solution. Instead, we seek tight bounds on this number.
Our main result is the following upper-bound and lower-bound:

Let G=![formula](https://latex.codecogs.com/svg.image?\left\langle\&space;V,E\&space;\right\rangle) 
be a balanced bipartite graph with n vertices and f edges and let
![formula](https://latex.codecogs.com/svg.image?c:E\&space;\rightarrow\&space;\{1,\&space;\ldots\&space;,k\})
be a proper edge-coloring of G in k colors. 
Then the number of rainbow perfect matchings in G is at most:

<p align="center">
    <image src="https://latex.codecogs.com/svg.image?\binom{k}{n}\cdot\left(\frac{1&plus;o\left(1\right)}{e^2}\right)^n\cdot\left(\frac{f}{k}\right)^n">   
</p>

and let G=![formula](https://latex.codecogs.com/svg.image?\left\langle\&space;V,E\&space;\right\rangle) 
be a balanced bipartite random graph with  vertices and f edges in 
expectation and let ![formula](https://latex.codecogs.com/svg.image?c:E\&space;\rightarrow\&space;\{1,\&space;\ldots\&space;,k\}) 
be a random edge-coloring of G in k colors. 
Then the number of rainbow perfect matchings in G is at least:

 <p align="center">
    <image src="https://latex.codecogs.com/svg.image?\binom{k}{n}\cdot\left(\frac{1-o\left(1\right)}{e^2}\right)^n\cdot\left(\frac{f}{k}\right)^n">   
</p>

In order to prove the upper-bound, we used the entropy method, which was already used to give a tight upper bound on the number of transversals in a Latin square.

To prove the lower-bound, we designed an algorithm which finds a transversal in a balanced bipartite complete graph and analyzed the number of the 
different transversals the algorithm can find (with high probability). 

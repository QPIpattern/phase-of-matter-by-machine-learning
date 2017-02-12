# phase-of-matter-by-machine-learning 
This project introduces unsupervised machine learning in the study of phase of matter in physics.
## Symmetry broken phases 
- Potts models(clock models) in square lattice. n=2 corresponds to Ising model.
- Monto Carlo method is used to simulate spin configurations at different temperatues. 
- High dimensional data of spin configurations are reduced by PCA method. 
- It is clear to see symmetric pattern after dimension reduction.
- **Theory of symmetry broken phase may be formulated by unsupervised machine learning**.

## KT phase transition   
In XY model, different phases are not marked by symmetry breaking
- Traditional dimension reduction cannot tell KT phase transition 
- Autoencoder method are used, including cnn, variational autoencoder(va), a combination of cnn and va. 
- At this stage, cnn method wins. But it is still not good to reconstuct the right spin configuration with vortex. 
- Further exploration is badly required. Autoencoder of topological objects such as vortex is not a topic of attention for the deep learning  community, but it seems not a trivial problem.

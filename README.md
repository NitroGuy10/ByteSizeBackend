# ByteSizeBackend

A video compression tool made for [HackTX 2022](https://devpost.com/software/bytesize)

Check out the [frontend](https://github.com/Abhishek-More/ByteSize) and the [machine learning part](https://github.com/anishfish2/ByteSizeML)

---

You need to clone ByteSizeML into a folder inside this directory called ByteSizeML. The "results" and "figure" folders should be moved up one level into the ByteSizeBackend folder, as should colorization_deploy_v2.prototxt, colorization_release_v2.caffemodel, and pts_in_hull.npy.

Install the requirements for both ByteSizeBackend and ByteSizeML into the same venv

This includes also installing PyTorch from your own tailored install command provide on the [PyTorch Website](https://pytorch.org/). Prefereably using Pip. For future reference, this project was created using PyTorch 1.12.1

To run:

`flask run`

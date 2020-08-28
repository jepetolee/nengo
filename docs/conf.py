# -*- coding: utf-8 -*-
#
# Automatically generated by nengo-bones, do not edit this file directly

import os

import nengo

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "nengo_sphinx_theme",
    "nengo_sphinx_theme.ext.backoff",
    "nengo_sphinx_theme.ext.redirects",
    "numpydoc",
    "nengo_sphinx_theme.ext.autoautosummary",
    "nengo_sphinx_theme.ext.resolvedefaults",
    "sphinx.ext.inheritance_diagram",
]

# -- sphinx.ext.autodoc
autoclass_content = "both"  # class and __init__ docstrings are concatenated
autodoc_default_options = {"members": None}
autodoc_member_order = "bysource"  # default is alphabetical

# -- sphinx.ext.doctest
doctest_global_setup = """
import nengo
import numpy as np
if np.__version__ >= '1.14':
    np.set_printoptions(legacy='1.13')
"""

# -- sphinx.ext.intersphinx
intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "sklearn": ("https://scikit-learn.org/dev", None),
}

# -- sphinx.ext.todo
todo_include_todos = True

# -- numpydoc config
numpydoc_show_class_members = False

# -- nbsphinx
nbsphinx_timeout = -1

# -- nengo_sphinx_theme.ext.autoautosummary
autoautosummary_change_modules = {
    "nengo": [
        "nengo.learning_rules.PES",
        "nengo.learning_rules.BCM",
        "nengo.learning_rules.Oja",
        "nengo.learning_rules.Voja",
        "nengo.neurons.Direct",
        "nengo.neurons.RectifiedLinear",
        "nengo.neurons.SpikingRectifiedLinear",
        "nengo.neurons.Sigmoid",
        "nengo.neurons.Tanh",
        "nengo.neurons.LIF",
        "nengo.neurons.LIFRate",
        "nengo.neurons.AdaptiveLIF",
        "nengo.neurons.AdaptiveLIFRate",
        "nengo.neurons.Izhikevich",
        "nengo.neurons.RegularSpiking",
        "nengo.neurons.PoissonSpiking",
        "nengo.neurons.StochasticSpiking",
        "nengo.synapses.LinearFilter",
        "nengo.synapses.Lowpass",
        "nengo.synapses.Alpha",
        "nengo.transforms.Dense",
        "nengo.transforms.Sparse",
        "nengo.transforms.Convolution",
        "nengo.config.Config",
    ],
    "nengo.builder": [
        "nengo.builder.operator.Operator",
        "nengo.builder.signal.Signal",
    ],
}

# -- sphinx
nitpicky = True
exclude_patterns = [
    "_build",
    "**/.ipynb_checkpoints",
]
linkcheck_timeout = 30
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
linkcheck_ignore = [r"http://localhost:\d+"]
linkcheck_anchors = True
default_role = "py:obj"
pygments_style = "sphinx"
user_agent = "nengo"

project = "Nengo"
authors = "Applied Brain Research"
copyright = "2013-2020 Applied Brain Research"
version = ".".join(nengo.__version__.split(".")[:2])  # Short X.Y version
release = nengo.__version__  # Full version, with tags

# -- HTML output
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "nengo_sphinx_theme"
html_title = "Nengo {0} docs".format(release)
htmlhelp_basename = "Nengo"
html_last_updated_fmt = ""  # Default output format (suppressed)
html_show_sphinx = False
html_favicon = os.path.join("_static", "favicon.ico")
html_theme_options = {
    "nengo_logo": "general-full-light.svg",
    "nengo_logo_color": "#a8acaf",
    "tagmanager_id": "GTM-KWCR2HN",
}
html_redirects = [
    ("backend_api.html", "backend-api.html"),
    (
        "examples/advanced/functions_and_tuning_curves.html",
        "examples/advanced/functions-and-tuning-curves.html",
    ),
    (
        "examples/advanced/inhibitory_gating.html",
        "examples/advanced/inhibitory-gating.html",
    ),
    (
        "examples/advanced/matrix_multiplication.html",
        "examples/advanced/matrix-multiplication.html",
    ),
    ("examples/advanced/nef_algorithm.html", "examples/advanced/nef-algorithm.html"),
    ("examples/advanced/nef_summary.html", "examples/advanced/nef-summary.html"),
    ("examples/basic/2d_representation.html", "examples/basic/2d-representation.html"),
    (
        "examples/basic/communication_channel.html",
        "examples/basic/communication-channel.html",
    ),
    ("examples/basic/many_neurons.html", "examples/basic/many-neurons.html"),
    ("examples/basic/single_neuron.html", "examples/basic/single-neuron.html"),
    ("examples/basic/two_neurons.html", "examples/basic/two-neurons.html"),
    (
        "examples/dynamics/controlled_integrator.html",
        "examples/dynamics/controlled-integrator.html",
    ),
    (
        "examples/dynamics/controlled_integrator2.html",
        "examples/dynamics/controlled-integrator2.html",
    ),
    (
        "examples/dynamics/controlled_oscillator.html",
        "examples/dynamics/controlled-oscillator.html",
    ),
    (
        "examples/dynamics/lorenz_attractor.html",
        "examples/dynamics/lorenz-attractor.html",
    ),
    (
        "examples/learning/learn_associations.html",
        "examples/learning/learn-associations.html",
    ),
    (
        "examples/learning/learn_communication_channel.html",
        "examples/learning/learn-communication-channel.html",
    ),
    ("examples/learning/learn_product.html", "examples/learning/learn-product.html"),
    ("examples/learning/learn_square.html", "examples/learning/learn-square.html"),
    (
        "examples/learning/learn_unsupervised.html",
        "examples/learning/learn-unsupervised.html",
    ),
    ("examples/networks/basal_ganglia.html", "examples/networks/basal-ganglia.html"),
    ("examples/networks/ensemble_array.html", "examples/networks/ensemble-array.html"),
    (
        "examples/networks/integrator_network.html",
        "examples/networks/integrator-network.html",
    ),
    ("examples/usage/delay_node.html", "examples/usage/delay-node.html"),
    (
        "examples/usage/network_design_advanced.html",
        "examples/usage/network-design-advanced.html",
    ),
    ("examples/usage/network_design.html", "examples/usage/network-design.html"),
    ("examples/usage/rectified_linear.html", "examples/usage/rectified-linear.html"),
    ("examples/usage/tuning_curves.html", "examples/usage/tuning-curves.html"),
    ("frontend_api.html", "frontend-api.html"),
    ("getting_started.html", "getting-started.html"),
    ("improving_performance.html", "improving-performance.html"),
    ("user_guide.html", "user-guide.html"),
]

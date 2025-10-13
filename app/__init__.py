"""Make 'app' a package and expose the Flask instance at top level."""
from .app import app  # now 'from app import app' works

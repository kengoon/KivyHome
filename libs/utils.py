from importlib import import_module

__all__ = ( 'importer', )


def importer(mod, cls):
    module = import_module(mod)

    return module if not cls else getattr(module, cls)


from .free_calldef import free_function_t


class function_template_t(free_function_t):
    def __init__(self, *args, template_params=None, **keywords):
        free_function_t.__init__(self, *args, **keywords)
        self._template_params = template_params or []

    def _get__cmp__call_items(self):
        """implementation details"""
        return self._template_params

    def __str__(self):
        # get full name of function template
        s = free_function_t.__str__(self)
        # preprend the template parameters
        t = [str(t_param) for t_param in self.template_params]
        return "template <%s> %s" % (', '.join(t), s)

    def __eq__(self, other):
        if not free_function_t.__eq__(self, other):
            return False

        if not isinstance(other, function_template_t):
            return False

        return self.template_params == other.template_params
    
    def __hash__(self):
        return (super(function_template_t, self).__hash__() ^
                hash(self.template_params))

    @property
    def template_params(self):
        """The template parameter list.
            @type: list of :class:`argument_t`"""
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        self._template_params = template_params
    
    # we don't override following methods
    # for now, even though we probably should at some point:
    # def function_type(self):
    # def create_decl_string(self, with_defaults=True):
    # def guess_calling_convention(self):

class template_param_kind_t(object):
    NON_TYPE = "non-type template parameter"
    TEMPLATE = "template template parameter"
    TYPE = "type template parameter"


class template_param_t(object):
    
    """
    class, that describes parameter of "template" declaration
    """
    
    def __init__(
            self,
            name='',
            decl_type=None,
            default_value=None,
            kind=None):
        object.__init__(self)

        self._name = name
        self._decl_type = decl_type
        self._default_value = default_value
        self._kind = kind

    def __str__(self):
        if self.kind == template_param_kind_t.TEMPLATE:
            s = "template <?> class %s" % self.name
        elif self.kind == template_param_kind_t.TYPE:
            s = "typename %s" % self.name
        elif self.kind == template_param_kind_t.NON_TYPE:
            if self.decl_type is None:
                # this should not happen
                return "[invalid template param]"
            s = "%s %s" % (self.decl_type, self.name)
        else:
            # this should not happen
            return "[invalid template param]"

        if self.default_value is None:
            return s
        
        return "%s=%s" % (s, self.default_value)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.name == other.name \
            and self.default_value == other.default_value \
            and self.decl_type == other.decl_type \
            and self.is_typename == other.is_typename \
            and self.is_template_template == other.is_template_template

    def __hash__(self):
        return (hash(self.__class__) ^
                hash(self.name) ^
                hash(self.default_value) ^
                hash(self.decl_type) ^
                hash(self.is_typename) ^
                hash(self.is_template_template))

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def name(self):
        """Parameter name.
            @type: str"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def default_value(self):
        """Parameter's default value or None.
            @type: str"""
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        self._default_value = default_value

    @property
    def decl_type(self):
        """Parameter's decl type if it is a non-type template parameter.
            @type: str"""
        return self._decl_type

    @decl_type.setter
    def decl_type(self, decl_type):
        self._decl_type = decl_type

    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, kind):
        self._kind = kind

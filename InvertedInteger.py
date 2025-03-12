class InvertedInteger:


      def __init__(self, obj):
            self.object = obj


      # overwrite "print"
      def __str__(self):
            return "<" + str(self.object) + ">"


      # define "*"
      def __mul__(self,other):
            return InvertedInteger(self.object
                                              + other.object
                                              + self.object*other.object)

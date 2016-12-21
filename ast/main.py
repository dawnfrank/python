import ast
PATH = "F:\\CODE\\ast\\test.py"
with open(PATH, "rb") as f:
	codestr = f.read()
tree=ast.parse(codestr,"test.py")

"""
#Module
print dir(tree)
print tree
print tree.body		
"""

"""
#Import
print dir(tree.body[0])
print tree.body[0].col_offset		#col
print tree.body[0].lineno			#row
print tree.body[0]._fields
print tree.body[0].names			#import name
"""

"""
#alias
print dir(tree.body[0].names[0])
print tree.body[0].names[0]._fields
print tree.body[0].names[0].name
print tree.body[0].names[0].asname
"""

"""
#Assign 
print dir(tree.body[1])
print tree.body[1].col_offset	#col
print tree.body[1].lineno		#row
print tree.body[1]._fields
print tree.body[1].targets		#leftValue
print tree.body[1].value		#rightValue
"""

"""
#Name
print dir(tree.body[1].targets[0])
print tree.body[1].targets[0].col_offset	#col
print tree.body[1].targets[0].lineno		#row
print tree.body[1].targets[0]._fields		
print tree.body[1].targets[0].id			#name
print tree.body[1].targets[0].ctx			
"""

"""
#Load | Store | Del | AugLoad | AugStore | Param
print dir(tree.body[1].targets[0].ctx)
print tree.body[1].targets[0].ctx._fields
"""

"""
#Num
print dir(tree.body[1].value)
print tree.body[1].value.col_offset		#col
print tree.body[1].value.lineno			#row
print tree.body[1].value._fields
print tree.body[1].value.n				#number
"""

"""
#ClassDef
print dir(tree.body[3])
print tree.body[3].col_offset			#col
print tree.body[3].lineno				#row
print tree.body[3]._fields	
print tree.body[3].name					#Class name
print tree.body[3].bases				#ast.Num
print tree.body[3].decorator_list
print tree.body[3].body					#class body
"""

"""
#FunctionDef
print dir(tree.body[3].body[0])
print tree.body[3].body[0].col_offset
print tree.body[3].body[0].lineno
print tree.body[3].body[0]._fields
print tree.body[3].body[0].args			#param
print tree.body[3].body[0].name			#function name
print tree.body[3].body[0].body
print tree.body[3].body[0].decorator_list
"""

"""
#arguments
print dir(tree.body[3].body[0].args)
print tree.body[3].body[0].args._fields
print tree.body[3].body[0].args.args		# param including default self,a,b
print tree.body[3].body[0].args.vararg		# *args list/tuple
print tree.body[3].body[0].args.kwarg		# **kwargs dict
print tree.body[3].body[0].args.defaults	# default param [num]]
"""

"""
#Param
print dir(tree.body[3].body[0].args.args[0].ctx)
print tree.body[3].body[0].args.args[0].ctx._fields
"""

"""
#For
print dir(tree.body[3].body[0].body[1])
print tree.body[3].body[0].body[1].col_offset	#col
print tree.body[3].body[0].body[1].lineno		#row
print tree.body[3].body[0].body[1]._fields
print tree.body[3].body[0].body[1].iter			#iterator ast.Call
print tree.body[3].body[0].body[1].orelse		#else
print tree.body[3].body[0].body[1].target		#i
print tree.body[3].body[0].body[1].body
"""

"""
#Call
print dir(tree.body[3].body[0].body[1].iter)
print tree.body[3].body[0].body[1].iter.col_offset
print tree.body[3].body[0].body[1].iter.lineno		#col
print tree.body[3].body[0].body[1].iter._fields		#row
print tree.body[3].body[0].body[1].iter.func		# function name -> range
print tree.body[3].body[0].body[1].iter.func.id
print tree.body[3].body[0].body[1].iter.args		#param
print tree.body[3].body[0].body[1].iter.keywords
print tree.body[3].body[0].body[1].iter.kwargs
print tree.body[3].body[0].body[1].iter.starargs	#*param
"""

"""
#print
print dir(tree.body[3].body[0].body[1].orelse[0])
print tree.body[3].body[0].body[1].orelse[0].col_offset	#col
print tree.body[3].body[0].body[1].orelse[0].lineno		#row
print tree.body[3].body[0].body[1].orelse[0]._fields
print tree.body[3].body[0].body[1].orelse[0].dest		#???
print tree.body[3].body[0].body[1].orelse[0].nl			#???
print tree.body[3].body[0].body[1].orelse[0].values		
"""

"""
#BinOp
print dir(tree.body[3].body[0].body[1].orelse[0].values[0])
print tree.body[3].body[0].body[1].orelse[0].values[0].col_offset
print tree.body[3].body[0].body[1].orelse[0].values[0].lineno
print tree.body[3].body[0].body[1].orelse[0].values[0]._fields
print tree.body[3].body[0].body[1].orelse[0].values[0].right	#right param
print tree.body[3].body[0].body[1].orelse[0].values[0].left		#left str
"""

"""
#Str
print dir(tree.body[3].body[0].body[1].orelse[0].values[0].left)
print tree.body[3].body[0].body[1].orelse[0].values[0].left.col_offset
print tree.body[3].body[0].body[1].orelse[0].values[0].left.lineno
print tree.body[3].body[0].body[1].orelse[0].values[0].left.s
"""

"""
#Return
print dir(tree.body[3].body[0].body[2])
print tree.body[3].body[0].body[2].col_offset
print tree.body[3].body[0].body[2].lineno
print tree.body[3].body[0].body[2]._fields
print tree.body[3].body[0].body[2].value
"""

"""
#Attribute
print dir(tree.body[3].body[0].body[2].value.func)
print tree.body[3].body[0].body[2].value.func.col_offset
print tree.body[3].body[0].body[2].value.func.lineno
print tree.body[3].body[0].body[2].value.func._fields
print tree.body[3].body[0].body[2].value.func.attr		#attr name
print tree.body[3].body[0].body[2].value.func.ctx		#????
print tree.body[3].body[0].body[2].value.func.value		#parent
"""

"""
#IF
print dir(tree.body[3].body[1].body[0])
print tree.body[3].body[1].body[0].col_offset
print tree.body[3].body[1].body[0].lineno
print tree.body[3].body[1].body[0]._fields
print tree.body[3].body[1].body[0].test			#sentence
print tree.body[3].body[1].body[0].body			#if body
print tree.body[3].body[1].body[0].orelse		#else
"""

"""
#Global
print dir(tree.body[3].body[2].body[0])
print tree.body[3].body[2].body[0]
print tree.body[3].body[2].body[0].col_offset
print tree.body[3].body[2].body[0].lineno
print tree.body[3].body[2].body[0]._fields
print tree.body[3].body[2].body[0].names
"""

"""
#Dict
print dir(tree.body[3].body[2].body[1].value)
print tree.body[3].body[2].body[1].value
print tree.body[3].body[2].body[1].value.col_offset
print tree.body[3].body[2].body[1].value.lineno
print tree.body[3].body[2].body[1].value._fields
print tree.body[3].body[2].body[1].value.keys
print tree.body[3].body[2].body[1].value.values
"""

"""
#Tuple
print dir(tree.body[3].body[2].body[2].target)
print tree.body[3].body[2].body[2].target
print tree.body[3].body[2].body[2].value.col_offset
print tree.body[3].body[2].body[2].value.lineno
print tree.body[3].body[2].body[2].target._fields
print tree.body[3].body[2].body[2].target.elts			#item of tuple
print tree.body[3].body[2].body[2].target.ctx
"""

"""
#Compare
print dir(tree.body[3].body[2].body[2].body[0].test)
print tree.body[3].body[2].body[2].body[0].test
print tree.body[3].body[2].body[2].body[0].test.col_offset
print tree.body[3].body[2].body[2].body[0].test.lineno
print tree.body[3].body[2].body[2].body[0].test._fields
print tree.body[3].body[2].body[2].body[0].test.left
print tree.body[3].body[2].body[2].body[0].test.ops
print tree.body[3].body[2].body[2].body[0].test.comparators
"""

"""
#Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn
print dir(tree.body[3].body[2].body[2].body[0].test.ops[0])
print tree.body[3].body[2].body[2].body[0].test.ops[0]
print tree.body[3].body[2].body[2].body[0].test.ops[0]._fields
"""


"""
#Pass | Break | Continue
print dir(tree.body[3].body[2].body[2].body[0].orelse[0])
print tree.body[3].body[2].body[2].body[0].orelse[0]
print tree.body[3].body[2].body[2].body[0].orelse[0].col_offset
print tree.body[3].body[2].body[2].body[0].orelse[0].lineno
print tree.body[3].body[2].body[2].body[0].orelse[0]._fields
"""

"""
#Delete
print dir(tree.body[3].body[2].body[3])
print tree.body[3].body[2].body[3]
print tree.body[3].body[2].body[3].col_offset
print tree.body[3].body[2].body[3].lineno
print tree.body[3].body[2].body[3]._fields
print tree.body[3].body[2].body[3].targets
"""

"""
#Subscript
print dir(tree.body[3].body[2].body[3].targets[0])
print tree.body[3].body[2].body[3].targets[0]
print tree.body[3].body[2].body[3].targets[0].col_offset
print tree.body[3].body[2].body[3].targets[0].lineno
print tree.body[3].body[2].body[3].targets[0]._fields
print tree.body[3].body[2].body[3].targets[0].value		#del name
print tree.body[3].body[2].body[3].targets[0].slice		#del Index
print tree.body[3].body[2].body[3].targets[0].ctx
"""

"""
#Index
print dir(tree.body[3].body[2].body[3].targets[0].slice)
print tree.body[3].body[2].body[3].targets[0].slice
print tree.body[3].body[2].body[3].targets[0].slice._fields
print tree.body[3].body[2].body[3].targets[0].slice.value
print tree.body[3].body[2].body[3].targets[0].slice.value.n
"""

"""
# Add | Sub | Mult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv
print dir(tree.body[3].body[3].body[0].value.op)
print tree.body[3].body[3].body[0].value.op._fields
"""

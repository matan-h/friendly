��    '      T  5   �      `  �   a  d   �  �   `  .     /   3  ^   c  ;   �  �   �  �   �  y   L  �   �  �   �  B   �	  d  �	  �   ]  �   [  8  �  �     �     @      A   A    �     �  �   �  \   `  �   �  _   e  h   �  [   .  o   �  (  �  l   #  2   �  q   �  /   5  �   e          &  z  ;  �   �  �   q  �   �  1   �  0   �  I     ?   b  �   �  �   9  �     '  �  +  �   c   �!  �  W"  5  $  �   M%  o  &  �   ~'  /  ~(  :   �)  R   �)  �  <*     �,  �   �,  c   �-  �   C.  �   /  x   �/  �   �/  �   �0  o   1  �   �2  A   3  s   V3  /   �3  �   �3  
   �4     �4        "   !          $           
                     &                                                     	                                   '         #             %                      In this case, the line identified above
        is more indented than expected and 
        does not match the indentation of the previous line.
         In this case, the line identified above
        was expected to begin a new indented block.
         In this case, the line identified above is
        less indented than the preceding one,
        and is not aligned vertically with another block of code.
         In this case, the sequence is a list.
         In this case, the sequence is a tuple.
         In your program, the name of the
        module that cannot be found is '{mod_name}'.
         In your program, the unknown name is '{var_name}'.
         The object that could not be imported is '{name}'.
        The module or package where it was 
        expected to be found is '{module}'.
         The variable that appears to cause the problem is '{var_name}'.
        Try inserting the statement
            global {var_name}
        as the first line inside your function.         Unfortunately, no additional information is available:
        the content of file '<string>' is not accessible.
     A ModuleNotFoundError exception indicates that you
    are trying to import a module that cannot be found by Python.
    This could be because you misspelled the name of the module
    or because it is not installed on your computer.
     A NameError exception indicates that a variable or
    function name is not known to Python.
    Most often, this is because there is a spelling mistake.
    However, sometimes it is because the name is used
    before being defined or given a value.
     A SyntaxError occurs when Python cannot understand your code.
     A TabError indicates that you have used both spaces
    and tab characters to indent your code.
    This is not allowed in Python.
    Indenting your code means to have block of codes aligned vertically
    by inserting either spaces or tab characters at the beginning of lines.
    Python's recommendation is to always use spaces to indent your code.
     A ZeroDivisionError occurs when you are attempting to divide
    a value by zero:
        result = my_variable / 0
    It can also happen if you calculate the remainder of a division
    using the modulo operator '%'
        result = my_variable % 0     An IndentationError occurs when a given line of code is
    not indented (aligned vertically with other lines) as expected.
     An IndexError occurs when you are try to get an item from a list,
    a tuple, or a similar object (sequence), by using an index which
    does not exists; typically, this is because the index you give
    is greater than the length of the sequence.
    Reminder: the first item of a sequence is at index 0.
     ArithmeticError is the base class for those built-in exceptions
    that are raised for various arithmetic errors.
    It is unusual that you are seeing this exception;
    normally, a more specific exception should have been raised.
     Currently, we cannot guess the likely cause of this error.

    Try to examine closely the line indicated as well as the line
    immediately above to see if you can identify some misspelled
    word, or missing symbols, like (, ), [, ], :, etc.

     Exception raised on line {linenumber} of file '{filename}'.
     Execution stopped on line {linenumber} of file '{filename}'.
     In Python, variables that are used inside a function are known as 
    local variables. Before they are used, they must be assigned a value.
    A variable that is used before it is assigned a value is assumed to
    be defined outside that function; it is known as a 'global'
    (or sometimes 'nonlocal') variable. You cannot assign a value to such
    a global variable inside a function without first indicating to
    Python that this is a global variable, otherwise you will see
    an UnboundLocalError.
     Likely cause:
{cause}     LookupError is the base class for the exceptions that are raised
    when a key or index used on a mapping or sequence is invalid.
    It can also be raised directly by codecs.lookup().
     My best guess: you meant to use Python's 'elif' keyword
    but wrote '{name}' instead

     My best guess: you tried to define {class_or_function}
    and did not use the correct syntax.
    The correct syntax is:
        def name ( optional_arguments ):
     My best guess: you wanted to define {class_}
    but forgot to add a colon ':' at the end

     My best guess: you were trying
    to assign a value to a Python keyword.
    This is not allowed.

     My best guess: you wrote a '{name}' loop but
    forgot to add a colon ':' at the end

     My best guess: you wrote a statement beginning with
    '{name}' but forgot to add a colon ':' at the end

     My best guess: you wrote an expression like
        {name} = something
    where <{name}>, on the left hand-side of the equal sign, is
    an actual number or string (what Python calls a 'literal'),
    and not the name of a variable.  Perhaps you meant to write:
        something = {name}

     My best guess: you wrote something like
        import X from Y
    instead of
        from Y import X

     No information is known about this exception.
     Python could not parse the file '{filename}'
    beyond the location indicated below by --> and ^.

{source}
     Python exception: 
        {name}: {value}
     This exception indicates that a certain object could not
    be imported from a module or package. Most often, this is
    because the name of the object is not spelled correctly.
 a class a function or method Project-Id-Version: 
POT-Creation-Date: 2019-04-30 16:04-0300
PO-Revision-Date: 2019-04-30 16:05-0300
Last-Translator: André Roberge <andre.roberge@gmail.com>
Language-Team: 
Language: fr
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.2.1
Plural-Forms: nplurals=2; plural=(n > 1);
         Dans ce cas-ci, la ligne indiquée ci-dessus par -->
        est plus indentée que ce qui était attendu et ne
        correspond pas à l'indentation de la ligne précédente.
         Dans ce cas-ci, la ligne indiquée ci-dessus par --> devrait
        normalement commencer un nouveau bloc de code indenté.
         Dans ce cas-ci, la ligne indiquée ci-dessus par -->
        est moins indentée que la ligne précédente
        et n’est pas alignée verticalement avec un autre bloc de code.
         Dans ce cas, la séquence est une liste.
         Dans ce cas, la séquence est un tuple.
         Dans votre programme, le nom du module inconnu est '{mod_name}'.
         Dans votre programme, le nom inconnu est '{var_name}'.
         L’objet qui n’a pas pu être importé est '{name}'.
        Le module ou le paquet d'où il devait être importé
        est '{module}'.
         La variable qui semble causer le problème est' {var_name} '.
        Essayez d’insérer l’instruction
            global {var_name}
        comme première ligne à l’intérieur de votre fonction.         Malheureusement, aucune information supplémentaire n’est disponible:
        le contenu du fichier '<string>' n’est pas accessible.
     Une exception ModuleNotFoundError indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en écrivant le nom du module
    ou parce qu’il n’est pas installé sur votre ordinateur.
     Une exception NameError indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
     Une exception de type SyntaxError se produit lorsque python ne peut pas comprendre votre code.
     Un exception de type TabError indique que vous avez utilisé des espaces ainsi que
    des caractères de tabulation pour indenter votre code.
    Cela n’est pas autorisé dans Python.
    L’indentation de votre code signifie que le bloc de codes est aligné verticalement 
    en insérant des espaces ou des tabulations au début des lignes.
    La recommandation de Python est de toujours utiliser des espaces pour indenter votre code.
     Une exception de type ZeroDivisionError se produit lorsque
    vous tentez de diviser une valeur par zéro:
        résultat = ma_variable / 0
    Ceci peut également se produire si vous calculez le reste d’une division 
    à l’aide de l’opérateur modulo '%'
        résultat = ma_variable % 0     Une exception de type IndentationError se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
     Un IndexError se produit lorsque vous essayez d’obtenir un élément
    d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un index qui
    n’existe pas; typiquement, c’est parce que l’index que vous donnez
    est plus grand que la longueur de la séquence.
    Rappel: le premier élément d'une séquence est à l'index 0.

     ArithmeticError est la classe de base pour les exceptions
    qui sont soulevées pour diverses erreurs arithmétiques.
    Il est inhabituel que vous voyiez cette exception;
    normalement, une exception plus spécifique aurait dû être soulevée.
     Présentement, nous ne pouvons pas deviner la cause probable de cette erreur.

    Essayez d’examiner attentivement la ligne indiquée ainsi que celle
    immédiatement au dessus pour voir si vous pouvez identifier
    un mot mal orthographié, ou des symboles manquants, comme (,), [,],:, etc.

     Exception levée à la ligne du fichier '{filename}'.
     L'exécution s'est arrêtée à la ligne {linenumber} du fichier '{filename}'
     En Python, les variables utilisées à l’intérieur d’une fonction sont appelées variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée être définie en
    dehors de cette fonction; elle est connu comme une variable «globale» ('global' ou parfois 'nonlocal').
    Vous ne pouvez pas assigner une valeur à une telle variable globale à l’intérieur d’une fonction
    sans d’abord confirmer à python qu’il s’agit d’une variable globale, sinon vous verrez
    une exception UnboundLocalError.
     Cause probable : 
{cause}     LookupError est la classe de base pour les exceptions qui sont levées
    lorsqu’une clé ou un index utilisé sur un tableau de correspondance ou une séquence est invalide.
    Elle peut également être levée directement par codecs.lookup().
     Ma meilleure hypothèse: vous avez écrit '{name}'
    au lieu d'utiliser le mot-clé 'elif'.

     Ma meilleure hypothèse: vous vouliez définir {class_or_function},
    mais vous avez fait des erreurs de syntaxe.
    La syntaxe correcte est:
        def nom ( arguments_optionnels ) :

     Ma meilleure hypothèse: vous vouliez définir {class_},
    mais vous avez oublié d’ajouter deux points ':' à la fin.

     Ma meilleure hypothèse: vous essayiez d’assigner une valeur à un mot clé Python.
    Ceci n’est pas permis.

     Ma meilleure hypothèse: vous vouliez débuter une boucle '{name}'
    mais vous avez oublié d’ajouter deux points ':' à la fin.

     Ma meilleure hypothèse: vous avez écrit un énoncé débutant avec
    '{name}' mais vous avez oublié d’ajouter deux points ':' à la fin.

     Ma meilleure hypothèse: vous avez écrit une expression comme
        {name} = variable
    où < {name} >, sur le côté gauche du signe égal, est ce que Python
    appelle un 'literal', c'est-à dire soit soit une chaîne de caractères ou un nombre,
    et non le nom d’une variable. Peut-être que vous vouliez plutôt écrire:
        variable = {name}

     Ma meilleure hypothèse: vous avez écrit quelque chose comme
        import X from Y
    au lieu de
        from Y import X


     Aucune information n'est connue au sujet de cette exception.
     Python peut seulement analyser le fichier '{filename}'
    jusqu'à l'endroit indiqué par --> et ^.

{source}
     Exception Python: 
        {name}: {value}
     Cette exception indique qu’un certain objet n’a pas pu
    être importé à partir d’un module ou d’un paquet. Très souvent, c’est
    parce que le nom de l’objet n’est pas écrit correctement.
 une classe une fonction ou une méthode 
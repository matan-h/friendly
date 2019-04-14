��          �   %   �      P  K   Q  L   �  >   �  f   )  �   �  d   *  �   �  ;   3  l   o  y   �  �   V  y     p   �  a   �  u   ]  �   �  �   �	  d  �
  �     �       �     �  2   �     �     �  z    E   �  ]   �  >   +  |   j  �   �  �   �  �   (  ?   �  �   &  {   �  �   #  �   �  �   �  �     �   �  +  N  #  z  �  �  5  ^  �   �  �  U     �!  A   �!  
   <"     G"                                                                       	                                     
                 
    Exception raised on line {linenumber} of file '{filename}'.

{source}
 
    Execution stopped on line {linenumber} of file '{filename}'.

{source}
 
    Python exception: 
        {name}: {value}

{explanation}         Currently, we cannot give you more information
        about the likely cause of this error.

         In this case, the line identified above
        is more indented than expected and 
        does not match the indentation of the previous line.
         In this case, the line identified above
        was expected to begin a new indented block.
         In this case, the line identified above is
        less indented than the preceding one,
        and is not aligned vertically with another block of code.
         In your program, the unknown name is '{var_name}'.
         My best guess: you were trying to assign a value
        to a Python keyword. This is not allowed.

         Python could not parse the file '{filename}'
        beyond the location indicated below by --> and ^.

{source}
         The variable that appears to cause the problem is '{var_name}'.
        Try inserting the statement
            global {var_name}
        as the first line inside your function.         Unfortunately, no additional information is available:
        the content of file '<string>' is not accessible.
        My best guess: you wanted to define {class_or_function}
       but forgot to add a colon ':' at the end

        My best guess: you wrote a '{name}' loop but
       forgot to add a colon ':' at the end

        My best guess: you wrote a statement beginning with
       '{name}' but forgot to add a colon ':' at the end

     A NameError exception indicates that a variable or
    function name is not known to Python.
    Most often, this is because there is a spelling mistake.
    However, sometimes it is because the name is used
    before being defined or given a value.
     A SyntaxError occurs when Python cannot understand your code.
    There could be many possible reasons:
    - a keyword might be misspelled;
    - a colon, :, or some other symbol like (, ], etc., might be missing;
    - etc.
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
     In Python, variables that are used inside a function are known as 
    local variables. Before they are used, they must be assigned a value.
    A variable that is used before it is assigned a value is assumed to
    be defined outside that function; it is known as a 'global'
    (or sometimes 'nonlocal') variable. You cannot assign a value to such
    a global variable inside a function without first indicating to
    Python that this is a global variable, otherwise you will see
    an UnboundLocalError.
     Likely cause:
{cause}     No information is known about this exception.
 a class a function or method Project-Id-Version: 
POT-Creation-Date: 2019-04-14 09:19-0300
PO-Revision-Date: 2019-04-14 09:20-0300
Last-Translator: André Roberge <andre.roberge@gmail.com>
Language-Team: 
Language: fr
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.2.1
Plural-Forms: nplurals=2; plural=(n > 1);
 
    Exception levée à la ligne du fichier '{filename}'.

{source}
 
    L'exécution s'est arrêtée à la ligne {linenumber} du fichier '{filename}'

{source}
 
    Exception Python: 
        {name}: {value}

{explanation}         Actuellement, nous ne pouvons pas vous donner plus d’informations
        sur la cause probable de cette erreur.

         Dans ce cas-ci, la ligne indiquée ci-dessus par -->
        est plus indentée que ce qui était attendu et ne
        correspond pas à l'indentation de la ligne précédente.
         Dans ce cas-ci, la ligne indiquée ci-dessus par --> devrait
        normalement commencer un nouveau bloc de code indenté.
         Dans ce cas-ci, la ligne indiquée ci-dessus par -->
        est moins indentée que la ligne précédente
        et n’est pas alignée verticalement avec un autre bloc de code.
         Dans votre programme, le nom inconnu est '{var_name}'.
         Ma meilleure hypothèse: vous essayiez d’assigner une valeur à un mot clé Python.
        Ceci n’est pas permis.

         Python peut seulement analyser le fichier '{filename}'
        jusqu'à l'endroit indiqué par --> et ^.

{source}
         La variable qui semble causer le problème est' {var_name} '.
        Essayez d’insérer l’instruction
            global {var_name}
        comme première ligne à l’intérieur de votre fonction.         Malheureusement, aucune information supplémentaire n’est disponible:
        le contenu du fichier '<string>' n’est pas accessible.
         Ma meilleure hypothèse: vous vouliez définir {class_or_function},
        mais vous avez oublié d’ajouter deux points ':' à la fin.

         Ma meilleure hypothèse: vous vouliez débuter une boucle '{name}'
        mais vous avez oublié d’ajouter deux points ':' à la fin.

         Ma meilleure hypothèse: vous avez écrit un énoncé débutant avec
        '{name}' mais vous avez oublié d’ajouter deux points ':' à la fin.

     Une exception NameError indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
     Une exception SyntaxError se produit lorsque python ne peut pas comprendre votre code.
    Il pourrait y avoir plusieurs raisons possibles:
    - un mot-clé peut être mal orthographié;
    - le symbole deux points, :, ou un autre symbole comme (,], etc., pourrait manquer;
    - etc.
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
     En Python, les variables utilisées à l’intérieur d’une fonction sont appelées variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée être définie en
    dehors de cette fonction; elle est connu comme une variable «globale» ('global' ou parfois 'nonlocal').
    Vous ne pouvez pas assigner une valeur à une telle variable globale à l’intérieur d’une fonction
    sans d’abord confirmer à python qu’il s’agit d’une variable globale, sinon vous verrez
    une exception UnboundLocalError.
     Cause probable : 
{cause}     Aucune information n'est connue au sujet de cette exception.
 une classe une fonction ou une méthode 
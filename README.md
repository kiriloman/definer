# Description

Find the definition for a given word in a given language.
It uses the oxforddictionaries API.

# Prerequisites

- Python 3

# Usage

- Run `python3 <path_to_main.py_file>`
- You will be greeted with
```bash
                    Input a word and 
                    the language the word is in 
                    separated by a comma (,).
                    Example: hello,en
                    
                    To exit, type -1.

```
- Input a word and a language separated by a comma. 
For example, `hello,en` will result in
```bash
            Definition of hello:
                
1. used as a greeting or to begin a phone conversation
        hello there, Katie!
2. an utterance of ‘hello’; a greeting
        she was getting polite nods and hellos from people
3. say or shout ‘hello’
        I pressed the phone button and helloed
```
while the `hablar,es` input will result in
```bash
            Definition of hablar:
                
1. Articular sonidos y palabras [una persona] para expresarse o comunicarse
        hablar alto
        hablar bajo
        hablar por los codos
        el niño está aprendiendo a hablar
2. Mantener una conversación [una persona] con otra u otras acerca de un asunto
        ayer hablé largamente con mi padre
3. Pronunciar [una persona] un discurso, generalmente en público
        el ministro hablará mañana en el Parlamento
        le dejaban hablar en algunas conmemoraciones y actos oficiales
4. Comunicarse mediante signos distintos de la palabra
        los sordomudos hablan mediante el lenguaje de las señas
5. Expresar [alguien] opiniones o juicios acerca de una cosa o una persona
        hablar mal de alguien
        hablar bien de alguien
        hablar mucho de política
        el asunto todavía dará mucho que hablar
6. Confesar o revelar la verdad de algo o decir todo lo que se sabe acerca de un asunto
        el prisionero dice que no hablará si no es en presencia de su abogado
7. Tratar un asunto de palabra o por escrito
        hablar de negocios
        hablar de la cuestión
        los autores no hablan de este punto
8. Acordar o convenir una cosa entre dos o más personas
        lo hemos hecho tal y como lo hablamos en su momento
9. Dar a una persona un determinado tratamiento
        hablar de usted
        hablar de tú
10. Recordar [una cosa] a otra o hacer pensar [una cosa] en otra
        los cielos y la tierra hablan de Dios
11. Tener [una obra artística] un determinado tema
        la pintura nos habla de la guerra
12. Tener una relación de noviazgo con otra persona
        Fernando habla a Gloria
        Fernando habla con Gloria
        mi vecina y su novio hablan desde hace dos años
13. Expresarse [una persona] en una determinada lengua
        hablar español
        hablar inglés
        hablar francés
14. Decir o comunicar una cosa con palabras
        hablar disparates
        hablar pestes
        hablar maravillas
        hablaba fantasías que se le ocurrían
15. Tratarse de palabra o tener relación social [una persona] con otra
        llevamos meses sin hablarnos
        no se hablan desde hace tiempo
```

- If the input is invalid or some error occurs using the external API, the user is informed of that.
For example, the input `hello,en,123` results in a parsing error
```bash
The instructions were not followed correctly for hello,en,123
```
while the input `some_word,es` results in an external API error
```bash
No entry found matching supplied source_lang, word and provided filters
```
- To exit the program, input `-1` and receive
```bash
До встречи дружище!
```

# pl-question-template
Starting point for building PrairieLearn Questions/Question Generators.


#### Basic Structure

* **info.json**
 * Basic configuration info for the question.
 * For the UID field, you must use this [UUID Generator](https://www.uuidtools.com/generate/v4).
* **question.html**
 * Formatting for the question, possibly using elements.
 * Find a list of elements for authoring questions [here](https://prairielearn.readthedocs.io/en/latest/elements/).
* **server.py**
 * Question generator file, with all of the randomization components.

**[This section](https://prairielearn.readthedocs.io/en/latest/question/) of the PL Docs has great resources as to how to properly author questions with elements.** See the `exampleQuestion/` folder for an example of a fully working question.

- what is standard error?

    s / sqrt(n)

    The standard deviation of the sample mean distribution.

- when to use different types of random number generation?

    ```python
    np.random.binomial(n, p, n_samples)
    ```

- how do we break down longer / more complex word problems?

    Look for the pieces of information that define one of the distributions
    we've covered. E.g. a mean and standard deviation, a rate over time, or a
    number of "trials" and a probability of success.

    Work towards finding the values for the parameters of the distribution.

    What will the outcome of the distribution look like?

- for binomial distribution problems:

    Figure out how you define "success". If a question is asking for the
    probabilty of the opposite of success, you could model this as 1 - P(success).

- what do we mean by using python on the quiz?
- will the quiz need to import the employees database (or something like this?)
- will we need to write SQL for the quiz? NO!
- will time be a factor?

- give time warnings when proctoring quiz.

> Let's imagine we end up with a p-value of .05. This means that if it's true
> that there is no difference in grades, and we ran the experiment 20 times, we
> would expect 1 out of the 20 experiments to tell us that there is a difference
> in grades, purely due to chance.

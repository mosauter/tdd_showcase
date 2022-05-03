# TDD Showcase
This is a simple project to showcase a TDD-Workflow for a simple beginner
workshop. It presents a small task/challenge and possible solutions
step-by-step.

# Task

Write a chunking algorithm in a TDD-Workflow for simple lists. The API should
look similar to this:

```python
def chunk(full_list: List[Any], chunksize: int) -> range:
    pass
```

One possible solution you find on the `solution`-branch or the tagged commits
for the single steps.

## Live-Templates

Just some simple live-templates I find useful for me personally when using
IntelliJ-ish IDEs and doing python unit-testing. You generally find them:

```
> Editor > Live Templates > Python group
```

### Test

Template text:
```python
def $PREFIX$_should_$TEST_DESCRIPTION$($PARAMETERS$) -> None:
    $END$
```

| Variable Name    | Expression                   | Default Value   | Skip if defined |
|----------------- | ---------------------------- | --------------- | --------------- |
| PREFIX           | `fileNameWithoutExtension()` | empty           | `true`          |
| TEST_DESCRIPTION | empty                        | empty           | `false`         |
| PARAMETERS       | empty                        | empty           | `false`         |

### Fixtures

Template text:
```python
@fixture
def $FIXTURE_NAME$($PARAMETER$) -> $RETURN$:
    $END$
```

| Variable Name | Expression | Default Value           | Skip if defined |
|-------------- | ---------- | ----------------------- | --------------- |
| FIXTURE_NAME  | empty      | empty                   | `false`         |
| PARAMETER     | empty      | `mocker: MockerFixture` | `false`         |
| RETURN        | empty      | `MagicMock`             | `false`         |

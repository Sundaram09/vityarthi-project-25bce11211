# Stopwatch & Alarm Clock -- Python Console Application

A simple and interactive **Python-based console application** that
provides two useful time utilities:

-   **Stopwatch** -- Measure elapsed time with millisecond precision\
-   **Alarm Clock** -- Set a custom alarm and get notified at the exact
    time

This project is beginner-friendly and demonstrates Python concepts like
loops, input validation, functions, and time management.

------------------------------------------------------------------------

## Features

### Stopwatch

-   Start and stop with ENTER\
-   Displays time in: **minutes, seconds, milliseconds**\
-   Useful for timing tasks or experiments

### Alarm Clock

-   Set **hour, minute, second**\
-   Validates input range\
-   Continuously checks system time\
-   Displays **"WAKE UP!"** at the exact moment\
-   Can be cancelled using **Ctrl + C**

### Additional Features

-   Clean, user-friendly menu\
-   Accepts multiple exit inputs (`3`, `q`, `exit`)\
-   Graceful handling of interrupts (Ctrl + C)

------------------------------------------------------------------------

## Technologies Used

-   **Python 3**
-   Built-in modules:
    -   `time`
    -   `datetime`
    -   `sys`

------------------------------------------------------------------------

## Project Structure

    main.py   → Contains the complete stopwatch and alarm logic

------------------------------------------------------------------------

## How to Run the Project

1.  Install **Python 3**
2.  Download or clone this project
3.  Open terminal / command prompt
4.  Run:

```{=html}
<!-- -->
```
    python main.py

------------------------------------------------------------------------

## Testing Instructions

### Stopwatch

-   Verify timer accuracy\
-   Check millisecond calculation\
-   Test fast start/stop

### Alarm

-   Set time 1--2 minutes ahead\
-   Verify it matches system time exactly\
-   Test invalid time inputs\
-   Try cancelling using Ctrl + C

------------------------------------------------------------------------

## Future Enhancements

-   Add alarm sound\
-   Add countdown timer\
-   Add lap feature\
-   Build GUI\
-   Save stopwatch logs

------------------------------------------------------------------------

## References

-   Python Documentation: https://docs.python.org/

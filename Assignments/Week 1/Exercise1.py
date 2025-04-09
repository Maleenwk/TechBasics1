{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial_id",
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "20e9ac6206a1d74b",
   "metadata": {},
   "source": [
    "## Your first Jupiter Notebook\n",
    "\n",
    "Hello everyone, this is a Jupiter notebook. This will be our main format for most of the exercise sessions.\n",
    "\n",
    "The cool thing about Jupiter notebook is that it combines code and explanations in one file and let you run python code directly from here.\n",
    "\n",
    "First, let's try to run the following cell:\n"
   ]
  },
  {
   "cell_type": "code",
   "id": "f8b08a9e68dc85d4",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T10:30:14.298917Z",
     "start_time": "2025-04-09T10:30:14.290580Z"
    }
   },
   "source": "print(\"Hello world!\")",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world!\n"
     ]
    }
   ],
   "execution_count": 1
  },
  {
   "cell_type": "markdown",
   "id": "fbb8fc0fbc841f14",
   "metadata": {},
   "source": [
    "You can always play around and edit the code cell to try your own code. But the program will not work unless the code is written exactly as it is above. For example, trying to run the print command without the quotation marks:"
   ]
  },
  {
   "cell_type": "code",
   "id": "649ed5f0f93e5893",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T10:31:35.017490Z",
     "start_time": "2025-04-09T10:31:35.012973Z"
    }
   },
   "source": "print(\"This works\")",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This works\n"
     ]
    }
   ],
   "execution_count": 4
  },
  {
   "cell_type": "markdown",
   "id": "55606f6304da9c49",
   "metadata": {},
   "source": [
    "You should also always close the parentheses, otherwise you will see another error message:"
   ]
  },
  {
   "cell_type": "code",
   "id": "d65d17702b8e770c",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T10:31:50.075951Z",
     "start_time": "2025-04-09T10:31:50.070378Z"
    }
   },
   "source": "print(\"Forgetful parentheses\")",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Forgetful parentheses\n"
     ]
    }
   ],
   "execution_count": 5
  },
  {
   "cell_type": "code",
   "id": "c53988c9eaf3a14f",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T10:32:02.724946Z",
     "start_time": "2025-04-09T10:32:02.720517Z"
    }
   },
   "source": [
    "print('Single quotation marks work as well')"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Single quotation marks work as well\n"
     ]
    }
   ],
   "execution_count": 6
  },
  {
   "cell_type": "markdown",
   "id": "f9ee27f4a8cf868e",
   "metadata": {},
   "source": [
    "You can also print multiple lines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3751bc98159ed943",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:15:23.063730Z",
     "start_time": "2025-04-07T21:15:23.055639Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Technical Basics I\n",
      "This is our first class of the semester\n",
      "Let's learn the print command in Python\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Technical Basics I!\")\n",
    "print(\"This is our first class of the semester.\")\n",
    "print(\"Let's learn the print function in Python.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2537fc3",
   "metadata": {},
   "source": [
    "Now it's your turn. Try to create a new code block below and print an emoticon: :-)"
   ]
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T10:34:11.917672Z",
     "start_time": "2025-04-09T10:34:11.912314Z"
    }
   },
   "cell_type": "code",
   "source": "print(\";)\")",
   "id": "2531bf9fc77340f",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ";)\n"
     ]
    }
   ],
   "execution_count": 8
  },
  {
   "cell_type": "markdown",
   "id": "edccb278",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29fea431a04a4919",
   "metadata": {},
   "source": [
    "You can even print arithmetic operations directly:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3b4e7414d19f36c8",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:25:20.160419Z",
     "start_time": "2025-04-07T21:25:20.147505Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "143\n",
      "44\n"
     ]
    }
   ],
   "source": [
    "print(3+4)\n",
    "print(11*13)\n",
    "print(8*5+4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fda3f293abd68c",
   "metadata": {},
   "source": [
    "Notice that there is no quotation marks around the arithmetic operations. Quotation marks are used to signify <i>strings</i>. We will talk more about strings next week. For now, what you put between the quotation marks will be printed exactly as it is.\n",
    "Notice the differences between the following two lines of code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc022cddb89eeff0",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:31:17.393173Z",
     "start_time": "2025-04-07T21:31:17.387732Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1+2-3\n"
     ]
    }
   ],
   "source": [
    "print(1+2-3)\n",
    "print(\"1+2-3\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa26abd63ca30ed5",
   "metadata": {},
   "source": [
    "You can even combine the two styles together, but don't forget to separate them with a comma."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bb3d2d5a74b0b8fb",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:42:18.324571Z",
     "start_time": "2025-04-07T21:42:18.320809Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is the result of 2025+2024: 4049\n"
     ]
    }
   ],
   "source": [
    "print(\"This is the result of 2025+2024:\", 2025+2024)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6011dfa02eb269d",
   "metadata": {},
   "source": [
    "And more commas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3a3ff2cca7a6815e",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:44:47.014185Z",
     "start_time": "2025-04-07T21:44:47.007933Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One hour has  3600 seconds. One day has  86400 minutes.\n"
     ]
    }
   ],
   "source": [
    "print(\"One hour has \", 60*60, \"seconds. One day has \", 60*60*24, \"minutes.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f722ecbd01347e47",
   "metadata": {},
   "source": [
    "Notice that all characters have the same width in your output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2572097965437886",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-07T21:36:09.355120Z",
     "start_time": "2025-04-07T21:36:09.352170Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----\n",
      "wwwww\n",
      "+++++\n"
     ]
    }
   ],
   "source": [
    "print(\"-----\")\n",
    "print(\"wwwww\")\n",
    "print(\"+++++\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e831d0dd25e9df",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "725afa7a4564cfe5",
   "metadata": {},
   "source": [
    "### Excercise 1\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6c572b47b46ff5d",
   "metadata": {},
   "source": [
    "Make a little piece of ASCII art with print functions in python. You can first try it out here in the notebook. After you are satisfied with your result, save it as a `.py` file\n"
   ]
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-04-09T11:00:52.916006Z",
     "start_time": "2025-04-09T11:00:52.912145Z"
    }
   },
   "cell_type": "code",
   "source": [
    "print(\" (\\ _ /)\")\n",
    "print(\" ( 'x' )\")\n",
    "print('c(\") (\")')"
   ],
   "id": "3d97a159296d2386",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " (\\ _ /)\n",
      " ( 'x' )\n",
      "c(\") (\")\n"
     ]
    }
   ],
   "execution_count": 21
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

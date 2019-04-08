# -*- coding: utf-8 -*-

"display utilities"
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from terminaltables import SingleTable, AsciiTable
from tabulate import tabulate
from colorama import init, Fore, Back, Style
from tensorflow.python.lib.io import file_io  # allows to write to GCP or local

init()  # colorama init


# Check if we are in ipython/colab
try:
    class_name = get_ipython().__class__.__name__
    if "Terminal" in class_name:
        IS_NOTEBOOK = False
    else:
        IS_NOTEBOOK = True

except NameError:
    IS_NOTEBOOK = False

if IS_NOTEBOOK:
    from tqdm import tqdm_notebook as tqdm
    from IPython.display import HTML
else:
    from tqdm import tqdm
    display = print


FG = 0
BG = 1


# TODO: create a set of HTML color to allows richer display in colab
colors = {
    'black': [Fore.BLACK, Back.BLACK],
    'red': [Fore.RED, Back.RED],
    'green': [Fore.GREEN, Back.GREEN],
    'yellow': [Fore.YELLOW, Back.YELLOW],
    'blue': [Fore.BLUE, Back.BLUE],
    'magenta': [Fore.MAGENTA, Back.MAGENTA],
    'cyan': [Fore.CYAN, Back.CYAN],
    'white': [Fore.WHITE, Back.WHITE],
}

styles = {
    "dim": Style.DIM,
    "normal": Style.NORMAL,
    "bright": Style.BRIGHT,
    "reset": Style.RESET_ALL
}


LOG = None


# Log functions
def set_log(filename):
    global LOG
    LOG = file_io.FileIO(filename, 'w')


def write_log(text):
    if LOG and not IS_NOTEBOOK:
        LOG.write(text + "\n")


# shorthand functions
def info(text, render=1):
    """ display a info

    Args:
        text (str): info message
        display (bool, optional): Defaults to True. Display or return settings

    Returns:
        str: setting value if display=False, None otherwise
    """
    color = 'green'
    s = "[Info] %s" % text

    write_log(s)
    if render:
        cprint(s, color)
    else:
        return colorize(s + '\n', color)


def warning(text, render=1):
    """ display a warning

    Args:
        text (str): warning message
        render (bool, optional): Defaults to True. render or return settings

    Returns:
        str: setting value if render=False, None otherwise
    """
    color = 'yellow'
    s = "[Warning] %s" % text

    write_log(s)
    if render:
        cprint(s, color)
    else:
        return colorize(s + '\n', color)


def fatal(text, render=1):
    """ display a fatal error, and die

    Args:
        text (str): fatal message
        render (bool, optional): Defaults to True. render or return settings

    Returns:
        str: setting value if render=False, None otherwise
    """
    color = 'white'
    bgcolor = 'red'
    s = "[FATAL] %s" % text

    write_log(s)
    if render:
        cprint(s, color, bgcolor)
    else:
        return colorize(s + '\n', color, bgcolor)        


def section(text):
    if IS_NOTEBOOK:
        section = '<h1 style="font-size:18px">' + text + '</h1>'
        cprint(section, '#4527A0')
    else:
        section = '[' + text + ']'
        cprint(section, 'yellow')
        write_log(section)


def subsection(text):
    if IS_NOTEBOOK:
        section = '<h2 style="font-size:16px">' + text + '</h2>'
        cprint(section, '#7E57C2')
    else:
        section = ' > ' + text + ''
        cprint(section, 'magenta', brightness='dim')
        write_log(section)


def setting(text, ident=1, idx=0, render=True):
    """ print setting

    Args:
        text (str): setting key:value as string
        ident (int, optional): Defaults to 0. Space indentation
        idx (int, optional): Defaults to 0. index of setting to rotate color.
        render (bool, optional): Defaults to True. render or return settings

    Returns:
        str: setting value if render=False, None otherwise
    """
    s = ' ' * ident
    s += '|-' + text
    if idx % 2:
        color = 'cyan'
    else:
        color = 'blue'

    write_log(s)
    if render:
        cprint(s, color)
    else:
        return colorize(s + '\n', color)


def highlight(text):
    if IS_NOTEBOOK:
        text = '<span style="font-size:14px"><b>' + text + '</b></span>'
        cprint(text, '#64DD17')
    else:
        write_log(text)
        cprint(text, 'green', brightness="bright")

# Charts


def print_bar_chart(val, max_val, title=None, left='', right='',
                    color='green', length=80):

    bar = make_bar_chart(val, max_val, title=title, left=left, right=right,
                         color=color, length=length)
    display(bar)


def make_bar_chart(val, max_val, title=None, left='', right='',
                   color='green', length=80):
    full_block = '█'
    empty_block = '░'
    half_block = '▒'

    # building the bar
    bar = ''
    num_full = length * val/float(max_val)
    bar += full_block * int(num_full)
    if not (num_full).is_integer():
        bar += half_block
    bar += empty_block * (length - len(bar))

    # colorize
    bar = colorize(bar, color)

    # adding left/right text if needed
    row = []
    if left:
        row.append(left)
    row.append(bar)
    if right:
        row.append(right)

    st = SingleTable([row], title)
    st.inner_column_border = False
    return st.table

# Low level function


def cprint(text, color, bg_color=None, brightness='normal'):
    """ Print given piece of text with color
    Args:
        text (str): text to colorize
        color (str): forground color
        bg_color (str, optional): Defaults to None. background color.
        brightness (str, optional): Defaults to normal. Text brightness.
    """

    text = colorize(text, color, bg_color, brightness)

    # HTMLify if needed
    if IS_NOTEBOOK and isinstance(text, str):
        text = HTML(text)
    display(text)


def colorize(text, color, bg_color=None, brightness='normal'):
    """ Colorize a given piece of text
    Args:
        text (str): text to colorize
        color (str): forground color
        bg_color (str, optional): Defaults to None. background color.
        brightness (str, optional): Defaults to normal. Text brightness.

    Returns:
        str: colorized text
    """

    if color not in colors and not IS_NOTEBOOK:
        msg = "Foreground color invalid:%s" % color
        raise ValueError(msg)

    if bg_color and bg_color not in colors and not IS_NOTEBOOK:
        "Background color invalid:%s" % bg_color
        raise ValueError(msg)

    if brightness not in brightness and not IS_NOTEBOOK:
        raise ValueError("Brightness invalid:" + brightness)

    text = str(text)  # in case user pass a float/int

    # foreground color
    if IS_NOTEBOOK:
        text = text.replace('\n', '<br>')
        h = '<span style="color:%s">' % color
        text = h + text
    else:
        text = colors[color][FG] + text
    # background if needed
    if bg_color and not IS_NOTEBOOK:
        text = colors[bg_color][BG] + text

    # brightness if neeed
    if brightness != 'normal' and not IS_NOTEBOOK:
        text = styles[brightness] + text

    # reset
    if IS_NOTEBOOK:
        text = text + '</span>'
    else:
        text = text + styles['reset']

    return text


# TABLE
def print_table(rows, title=None, indent=0):
    """ Print data as a nicely formated ascii table
    Args:
        rows (list(list)): data to display as list of lists.
        title (str, optional): Defaults to None. Table title
    """
    table = make_table(rows, title)

    if indent and not IS_NOTEBOOK:
        indent = " " * indent
        out = []
        for line in table.split("\n"):
            out.append(indent + line)
        table = "\n".join(out)

    write_log(table)
    display(table)


def make_table(rows, title=None):
    """ Format list as a pretty ascii table
    Args:
        rows (list(list)): data to display as list of lists.
        title (str, optional): Defaults to None. Table title
    Returns:
        str: string representing table
    """
    if IS_NOTEBOOK:
        headers = rows[0]
        body = rows[1:]
        table = tabulate(body, headers, tablefmt="html")
        table = HTML(table)
    else:
        st = SingleTable(rows, title)
        table = st.table
    return table


def make_combined_table(array_rows):
    """ Build a table of tables

    Args:
        array_rows (list(list)): Array of tables rows to combine
    Returns:
        str: string representing table
    """

    if IS_NOTEBOOK:
        # compute the size for each col
        col_size = str(int(100 / len(array_rows)) - 5) + '%'
        gtc = [col_size] * len(array_rows)
        table = """
        <style>
            .wrapper {
                display: grid;
                grid-template-columns: %s;
                grid-gap: 10px;
            }
        </style>
        <div  class="wrapper">
        """ % (" ".join(gtc))
        for rows in array_rows:
            table += '<div>'
            headers = rows[0]
            body = rows[1:]
            table += tabulate(body, headers, tablefmt="html")
            table += '</div>'
        table += "</div>"
        return HTML(table)
    else:
        tables = []
        for rows in array_rows:
            tables.append(make_table(rows))
        combined_table = AsciiTable([tables])
        combined_table.outer_border = False
        combined_table.inner_column_border = False
        return combined_table.table


def print_combined_table(array_rows):
    """ Build a table of tables and print it

    Args:
        array_rows (list(list)): Array of tables rows to combine
    """
    table = make_combined_table(array_rows)
    write_log(table)
    display(table)


def get_progress_bar(*args, **kwargs):
    """ Returns a new tqdm progress bar appropriate for the current display.

    Returns:
        tqdm progress bar.
    """

    return tqdm(*args, **kwargs)
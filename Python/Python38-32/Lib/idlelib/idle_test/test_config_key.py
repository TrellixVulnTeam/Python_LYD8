"""Test config_key, coverage 98%.

Coverage is effectively 100%.  Tkinter dialog is mocked, Mac-only line
may be skipped, and dummy function in bind test should not be called.
Not tested: exit with 'self.advanced or self.keys_ok(keys)) ...' False.
"""

from idlelib import config_key
from spider.test import requires
import unittest
from unittest import mock
from tkinter import Tk, TclError
from idlelib.idle_test.mock_idle import Func
from idlelib.idle_test.mock_tk import Mbox_func

gkd = config_key.GetKeysDialog


class ValidationTest(unittest.TestCase):
    "Test validation methods: ok, keys_ok, bind_ok."

    class Validator(gkd):
        def __init__(self, *args, **kwargs):
            config_key.GetKeysDialog.__init__(self, *args, **kwargs)
            class list_keys_final:
                get = Func()
            self.list_keys_final = list_keys_final
        get_modifiers = Func()
        showerror = Mbox_func()

    @classmethod
    def setUpClass(cls):
        requires('gui')
        cls.root = Tk()
        cls.root.withdraw()
        keylist = [['<Key-F12>'], ['<Control-Key-x>', '<Control-Key-X>']]
        cls.dialog = cls.Validator(
            cls.root, 'Title', '<<Test>>', keylist, _utest=True)

    @classmethod
    def tearDownClass(cls):
        cls.dialog.cancel()
        cls.root.update_idletasks()
        cls.root.destroy()
        del cls.dialog, cls.root

    def setUp(self):
        self.dialog.showerror.message = ''
    # A test that needs a particular final key value should set it.
    # A test that sets a non-blank modifier list should reset it to [].

    def test_ok_empty(self):
        self.dialog.key_string.set(' ')
        self.dialog.ok()
        self.assertEqual(self.dialog.result, '')
        self.assertEqual(self.dialog.showerror.message, 'No key specified.')

    def test_ok_good(self):
        self.dialog.key_string.set('<Key-F11>')
        self.dialog.list_keys_final.get.result = 'F11'
        self.dialog.ok()
        self.assertEqual(self.dialog.result, '<Key-F11>')
        self.assertEqual(self.dialog.showerror.message, '')

    def test_keys_no_ending(self):
        self.assertFalse(self.dialog.keys_ok('<Control-Shift'))
        self.assertIn('Missing the final', self.dialog.showerror.message)

    def test_keys_no_modifier_bad(self):
        self.dialog.list_keys_final.get.result = 'A'
        self.assertFalse(self.dialog.keys_ok('<Key-A>'))
        self.assertIn('No modifier', self.dialog.showerror.message)

    def test_keys_no_modifier_ok(self):
        self.dialog.list_keys_final.get.result = 'F11'
        self.assertTrue(self.dialog.keys_ok('<Key-F11>'))
        self.assertEqual(self.dialog.showerror.message, '')

    def test_keys_shift_bad(self):
        self.dialog.list_keys_final.get.result = 'a'
        self.dialog.get_modifiers.result = ['Shift']
        self.assertFalse(self.dialog.keys_ok('<a>'))
        self.assertIn('shift modifier', self.dialog.showerror.message)
        self.dialog.get_modifiers.result = []

    def test_keys_dup(self):
        for mods, final, seq in (([], 'F12', '<Key-F12>'),
                                 (['Control'], 'x', '<Control-Key-x>'),
                                 (['Control'], 'X', '<Control-Key-X>')):
            with self.subTest(m=mods, f=final, s=seq):
                self.dialog.list_keys_final.get.result = final
                self.dialog.get_modifiers.result = mods
                self.assertFalse(self.dialog.keys_ok(seq))
                self.assertIn('already in use', self.dialog.showerror.message)
        self.dialog.get_modifiers.result = []

    def test_bind_ok(self):
        self.assertTrue(self.dialog.bind_ok('<Control-Shift-Key-a>'))
        self.assertEqual(self.dialog.showerror.message, '')

    def test_bind_not_ok(self):
        self.assertFalse(self.dialog.bind_ok('<Control-Shift>'))
        self.assertIn('not accepted', self.dialog.showerror.message)


class ToggleLevelTest(unittest.TestCase):
    "Test toggle between Basic and Advanced frames."

    @classmethod
    def setUpClass(cls):
        requires('gui')
        cls.root = Tk()
        cls.root.withdraw()
        cls.dialog = gkd(cls.root, 'Title', '<<Test>>', [], _utest=True)

    @classmethod
    def tearDownClass(cls):
        cls.dialog.cancel()
        cls.root.update_idletasks()
        cls.root.destroy()
        del cls.dialog, cls.root

    def test_toggle_level(self):
        dialog = self.dialog

        def stackorder():
            """Get the stack order of the children of the frame.

            winfo_children() stores the children in stack order, so
            this can be used to check whether a frame is above or
            below another one.
            """
            for index, child in enumerate(dialog.frame.winfo_children()):
                if child._name == 'keyseq_basic':
                    basic = index
                if child._name == 'keyseq_advanced':
                    advanced = index
            return basic, advanced

        # New window starts at basic level.
        self.assertFalse(dialog.advanced)
        self.assertIn('Advanced', dialog.button_level['text'])
        basic, advanced = stackorder()
        self.assertGreater(basic, advanced)

        # Toggle to advanced.
        dialog.toggle_level()
        self.assertTrue(dialog.advanced)
        self.assertIn('Basic', dialog.button_level['text'])
        basic, advanced = stackorder()
        self.assertGreater(advanced, basic)

        # Toggle to basic.
        dialog.button_level.invoke()
        self.assertFalse(dialog.advanced)
        self.assertIn('Advanced', dialog.button_level['text'])
        basic, advanced = stackorder()
        self.assertGreater(basic, advanced)


class KeySelectionTest(unittest.TestCase):
    "Test selecting key on Basic frames."

    class Basic(gkd):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            class list_keys_final:
                get = Func()
                select_clear = Func()
                yview = Func()
            self.list_keys_final = list_keys_final
        def set_modifiers_for_platform(self):
            self.modifiers = ['foo', 'bar', 'BAZ']
            self.modifier_label = {'BAZ': 'ZZZ'}
        showerror = Mbox_func()

    @classmethod
    def setUpClass(cls):
        requires('gui')
        cls.root = Tk()
        cls.root.withdraw()
        cls.dialog = cls.Basic(cls.root, 'Title', '<<Test>>', [], _utest=True)

    @classmethod
    def tearDownClass(cls):
        cls.dialog.cancel()
        cls.root.update_idletasks()
        cls.root.destroy()
        del cls.dialog, cls.root

    def setUp(self):
        self.dialog.clear_key_seq()

    def test_get_modifiers(self):
        dialog = self.dialog
        gm = dialog.get_modifiers
        eq = self.assertEqual

        # Modifiers are set on/off by invoking the checkbutton.
        dialog.modifier_checkbuttons['foo'].invoke()
        eq(gm(), ['foo'])

        dialog.modifier_checkbuttons['BAZ'].invoke()
        eq(gm(), ['foo', 'BAZ'])

        dialog.modifier_checkbuttons['foo'].invoke()
        eq(gm(), ['BAZ'])

    @mock.patch.object(gkd, 'get_modifiers')
    def test_build_key_string(self, mock_modifiers):
        dialog = self.dialog
        key = dialog.list_keys_final
        string = dialog.key_string.get
        eq = self.assertEqual

        key.get.result = 'a'
        mock_modifiers.return_value = []
        dialog.build_key_string()
        eq(string(), '<Key-a>')

        mock_modifiers.return_value = ['mymod']
        dialog.build_key_string()
        eq(string(), '<mymod-Key-a>')

        key.get.result = ''
        mock_modifiers.return_value = ['mymod', 'test']
        dialog.build_key_string()
        eq(string(), '<mymod-test>')

    @mock.patch.object(gkd, 'get_modifiers')
    def test_final_key_selected(self, mock_modifiers):
        dialog = self.dialog
        key = dialog.list_keys_final
        string = dialog.key_string.get
        eq = self.assertEqual

        mock_modifiers.return_value = ['Shift']
        key.get.result = '{'
        dialog.final_key_selected()
        eq(string(), '<Shift-Key-braceleft>')


class CancelTest(unittest.TestCase):
    "Simulate user clicking [Cancel] button."

    @classmethod
    def setUpClass(cls):
        requires('gui')
        cls.root = Tk()
        cls.root.withdraw()
        cls.dialog = gkd(cls.root, 'Title', '<<Test>>', [], _utest=True)

    @classmethod
    def tearDownClass(cls):
        cls.dialog.cancel()
        cls.root.update_idletasks()
        cls.root.destroy()
        del cls.dialog, cls.root

    def test_cancel(self):
        self.assertEqual(self.dialog.winfo_class(), 'Toplevel')
        self.dialog.button_cancel.invoke()
        with self.assertRaises(TclError):
            self.dialog.winfo_class()
        self.assertEqual(self.dialog.result, '')


class HelperTest(unittest.TestCase):
    "Test module level helper functions."

    def test_translate_key(self):
        tr = config_key.translate_key
        eq = self.assertEqual

        # Letters return unchanged with no 'Shift'.
        eq(tr('q', []), 'Key-q')
        eq(tr('q', ['Control', 'Alt']), 'Key-q')

        # 'Shift' uppercases single lowercase letters.
        eq(tr('q', ['Shift']), 'Key-Q')
        eq(tr('q', ['Control', 'Shift']), 'Key-Q')
        eq(tr('q', ['Control', 'Alt', 'Shift']), 'Key-Q')

        # Convert key name to keysym.
        eq(tr('Page Up', []), 'Key-Prior')
        # 'Shift' doesn't change case when it's not a single char.
        eq(tr('*', ['Shift']), 'Key-asterisk')


if __name__ == '__main__':
    unittest.main(verbosity=2)

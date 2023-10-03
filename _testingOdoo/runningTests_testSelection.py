# Running tests
'''
Tests are automatically run when installing or updating modules if --test-enable was enabled when starting the Odoo server.

Test selection
In Odoo, Python tests can be tagged to facilitate the test selection when running tests.

Subclasses of odoo.tests.common.BaseCase (usually through TransactionCase, SavepointCase or HttpCase) are automatically tagged with standard and at_install by default.

Invocation
--test-tags can be used to select/filter tests to run on the command-line. It implies --test-enable, so it’s not necessary to specify --test-enable when using --test-tags.

This option defaults to +standard meaning tests tagged standard (explicitly or implicitly) will be run by default when starting Odoo with --test-enable.

When writing tests, the tagged() decorator can be used on test classes to add or remove tags.

The decorator’s arguments are tag names, as strings.

 Danger

tagged() is a class decorator, it has no effect on functions or methods

Tags can be prefixed with the minus (-) sign, to remove them instead of add or select them e.g. if you don’t want your test to be executed by default you can remove the standard tag:

from odoo.tests import TransactionCase, tagged

@tagged('-standard', 'nice')
class NiceTest(TransactionCase):
    ...
This test will not be selected by default, to run it the relevant tag will have to be selected explicitly:

 odoo-bin --test-tags nice
Note that only the tests tagged nice are going to be executed. To run both nice and standard tests, provide multiple values to --test-tags: on the command-line, values are additive (you’re selecting all tests with any of the specified tags)

 odoo-bin --test-tags nice,standard
The config switch parameter also accepts the + and - prefixes. The + prefix is implied and therefore, totally optional. The - (minus) prefix is made to deselect tests tagged with the prefixed tags, even if they are selected by other specified tags e.g. if there are standard tests which are also tagged as slow you can run all standard tests except the slow ones:

 odoo-bin --test-tags 'standard,-slow'
When you write a test that does not inherit from the BaseCase, this test will not have the default tags, you have to add them explicitly to have the test included in the default test suite. This is a common issue when using a simple unittest.TestCase as they’re not going to get run:

import unittest
from odoo.tests import tagged

@tagged('standard', 'at_install')
class SmallTest(unittest.TestCase):
    ...
Besides tags you can also specify specific modules, classes or functions to test. The full syntax of the format accepted by --test-tags is:

[-][tag][/module][:class][.method]
So if you want to test the stock_account module, you can use:

 odoo-bin --test-tags /stock_account
If you want to test a specific function with a unique name, it can be specified directly:

 odoo-bin --test-tags .test_supplier_invoice_forwarded_by_internal_user_without_supplier
This is equivalent to

 odoo-bin --test-tags /account:TestAccountIncomingSupplierInvoice.test_supplier_invoice_forwarded_by_internal_user_without_supplier
if the name of the test is unambiguous. Multiple modules, classes and functions can be specified at once separated by a , like with regular tags.

Special tags
standard: All Odoo tests that inherit from BaseCase are implicitly tagged standard. --test-tags also defaults to standard.

That means untagged test will be executed by default when tests are enabled.

at_install: Means that the test will be executed right after the module installation and before other modules are installed. This is a default implicit tag.

post_install: Means that the test will be executed after all the modules are installed. This is what you want for HttpCase tests most of the time.

Note that this is not exclusive with at_install, however since you will generally not want both post_install is usually paired with -at_install when tagging a test class.

Examples
 Important

Tests will be executed only in installed modules. If you’re starting from a clean database, you’ll need to install the modules with the -i switch at least once. After that it’s no longer needed, unless you need to upgrade the module, in which case -u can be used. For simplicity, those switches are not specified in the examples below.

Run only the tests from the sale module:

 odoo-bin --test-tags /sale
Run the tests from the sale module but not the ones tagged as slow:

 odoo-bin --test-tags '/sale,-slow'
Run only the tests from stock or tagged as slow:

 odoo-bin --test-tags '-standard, slow, /stock'
 Note

-standard is implicit (not required), and present for clarity

'''

#Odoo provides support for testing modules using Python’s unittest library.
"""
To write tests:

simply define a 'tests' sub-package in your module, 
it will be automatically inspected for test modules. 
Test modules should have a name starting with test_ and should be imported from tests/__init__.py, e.g.
"""
#           your_module
#           ├── ...
#           ├── tests
#           |   ├── __init__.py
#           |   ├── test_bar.py
#           |   └── test_foo.py
'''
__init__.py
contains:
from . import test_foo, test_bar
'''

Warning
'''
test modules which are not imported from tests/__init__.py will not be run
The test runner will simply run any test case, 
as described in the official unittest documentation, 
but Odoo provides a number of utilities and helpers related to testing Odoo content (modules, mainly):
'''

#   class odoo.tests.common.TransactionCase(methodName='runTest')[source]
'''
#   Test class in which all test methods are run in a single transaction, 
#   but each test method is run in a sub-transaction managed by a savepoint. 
#   The transaction’s cursor is always closed without committing.

#   The data setup common to all methods should be done in the class method setUpClass,
#   so that it is done once for all test methods. This is useful for test cases containing fast
#   tests but with significant database setup common to all cases (complex in-db test data).

#   After being run, each test method cleans up the record cache and the registry cache.
#   However, there is no cleanup of the registry models and fields.If a test modifies the registry 
#   (custom models and/or fields), it should prepare the necessary cleanup 
#   (self.registry.reset_changes()).
'''

#   browse_ref(xid)
'''
#    [https://github.com/odoo/odoo/blob/16.0/odoo/tests/common.py#L286]
#    Returns a record object for the provided external identifier

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
BaseModel

ref(xid)[source]
Returns database ID for the provided external identifier, shortcut for _xmlid_lookup

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
registered id

class odoo.tests.common.SingleTransactionCase(methodName='runTest')[source]
TestCase in which all test methods are run in the same transaction, the transaction is started with the first test method and rolled back at the end of the last.

browse_ref(xid)[source]
Returns a record object for the provided external identifier

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
BaseModel

ref(xid)[source]
Returns database ID for the provided external identifier, shortcut for _xmlid_lookup

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
registered id

class odoo.tests.common.SavepointCase(methodName='runTest')[source]
class odoo.tests.common.HttpCase(methodName='runTest')[source]
Transactional HTTP TestCase with url_open and Chrome headless helpers.

browse_ref(xid)[source]
Returns a record object for the provided external identifier

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
BaseModel

browser_js(url_path, code, ready='', login=None, timeout=60, cookies=None, error_checker=None, watch=False, **kw)[source]
Test js code running in the browser - optionnally log as ‘login’ - load page given by url_path - wait for ready object to be available - eval(code) inside the page - open another chrome window to watch code execution if watch is True

To signal success test do: console.log(‘test successful’) To signal test failure raise an exception or call console.error with a message. Test will stop when a failure occurs if error_checker is not defined or returns True for this message

ref(xid)[source]
Returns database ID for the provided external identifier, shortcut for _xmlid_lookup

Parameters
xid – fully-qualified external identifier, in the form module.identifier

Raise
ValueError if not found

Returns
registered id

odoo.tests.common.tagged(*tags)[source]
A decorator to tag BaseCase objects.

Tags are stored in a set that can be accessed from a ‘test_tags’ attribute.

A tag prefixed by ‘-‘ will remove the tag e.g. to remove the ‘standard’ tag.

By default, all Test classes from odoo.tests.common have a test_tags attribute that defaults to ‘standard’ and ‘at_install’.

When using class inheritance, the tags ARE inherited.

By default, tests are run once right after the corresponding module has been installed. Test cases can also be configured to run after all modules have been installed, and not run right after the module installation:

# coding: utf-8
from odoo.tests import HttpCase, tagged

# This test should only be executed after all modules have been installed.
@tagged('-at_install', 'post_install')
class WebsiteVisitorTests(HttpCase):
  def test_create_visitor_on_tracked_page(self):
      Page = self.env['website.page']
The most common situation is to use TransactionCase and test a property of a model in each method:

class TestModelA(common.TransactionCase):
    def test_some_action(self):
        record = self.env['model.a'].create({'field': 'value'})
        record.some_action()
        self.assertEqual(
            record.field,
            expected_field_value)

    # other tests...
 Note

Test methods must start with test_

class odoo.tests.common.Form(recordp, view=None)[source]
Server-side form view implementation (partial)

Implements much of the “form view” manipulation flow, such that server-side tests can more properly reflect the behaviour which would be observed when manipulating the interface:

call default_get and the relevant onchanges on “creation”

call the relevant onchanges on setting fields

properly handle defaults & onchanges around x2many fields

Saving the form returns the created record if in creation mode.

Regular fields can just be assigned directly to the form, for Many2one fields assign a singleton recordset:

# empty recordset => creation mode
f = Form(self.env['sale.order'])
f.partner_id = a_partner
so = f.save()
When editing a record, using the form as a context manager to automatically save it at the end of the scope:

with Form(so) as f2:
    f2.payment_term_id = env.ref('account.account_payment_term_15days')
    # f2 is saved here
For Many2many fields, the field itself is a M2MProxy and can be altered by adding or removing records:

with Form(user) as u:
    u.groups_id.add(env.ref('account.group_account_manager'))
    u.groups_id.remove(id=env.ref('base.group_portal').id)
Finally One2many are reified as O2MProxy.

Because the One2many only exists through its parent, it is manipulated more directly by creating “sub-forms” with the new() and edit() methods. These would normally be used as context managers since they get saved in the parent record:

with Form(so) as f3:
    # add support
    with f3.order_line.new() as line:
        line.product_id = env.ref('product.product_product_2')
    # add a computer
    with f3.order_line.new() as line:
        line.product_id = env.ref('product.product_product_3')
    # we actually want 5 computers
    with f3.order_line.edit(1) as line:
        line.product_uom_qty = 5
    # remove support
    f3.order_line.remove(index=0)
    # SO is saved here
Parameters
recordp (odoo.models.Model) – empty or singleton recordset. An empty recordset will put the view in “creation” mode and trigger calls to default_get and on-load onchanges, a singleton will put it in “edit” mode and only load the view’s data.

view (int | str | odoo.model.Model) – the id, xmlid or actual view object to use for onchanges and view constraints. If none is provided, simply loads the default view for the model.

New in version 12.0.

save()[source]
Saves the form, returns the created record if applicable

does not save readonly fields

does not save unmodified fields (during edition) — any assignment or onchange return marks the field as modified, even if set to its current value

Raises
AssertionError – if the form has any unfilled required field

class odoo.tests.common.M2MProxy[source]
Behaves as a Sequence of recordsets, can be indexed or sliced to get actual underlying recordsets.

add(record)[source]
Adds record to the field, the record must already exist.

The addition will only be finalized when the parent record is saved.

clear()[source]
Removes all existing records in the m2m

remove(id=None, index=None)[source]
Removes a record at a certain index or with a provided id from the field.

class odoo.tests.common.O2MProxy[source]
edit(index)[source]
Returns a Form to edit the pre-existing One2many record.

The form is created from the list view if editable, or the field’s form view otherwise.

Raises
AssertionError – if the field is not editable

new()[source]
Returns a Form for a new One2many record, properly initialised.

The form is created from the list view if editable, or the field’s form view otherwise.

Raises
AssertionError – if the field is not editable

remove(index)[source]
Removes the record at index from the parent form.

Raises
AssertionError – if the field is not editable

'''
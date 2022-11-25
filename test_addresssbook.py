import pytest
from main import Contacts,Addressbook,MultipleAddressbook

@pytest.fixture
def contacts():
    return Contacts('ashish','p','sangli','mh','sangli',416416,9156524636,'ashish32@gmail.com')

@pytest.fixture
def contacts1():
    return Contacts('ashish','patil','sangli','mh','sangli',416416,9156524636,'ashish32@gmail.com')

@pytest.fixture
def addressbook():
    return Addressbook('work')

@pytest.fixture
def multi_addressbook():
    return MultipleAddressbook()

def test_addbook(contacts,addressbook):
    assert len(addressbook.people) == 0
    addressbook.add_person(contacts)
    assert len(addressbook.people) == 1

def test_deletebook(contacts,addressbook):
    addressbook.add_person(contacts)
    assert len(addressbook.people) == 1
    addressbook.delete('ashish')
    assert len(addressbook.people) == 0

def test_addmultibook(contacts,addressbook,multi_addressbook):
    assert len(multi_addressbook.multi_book) == 0
    addressbook.add_person(contacts)
    multi_addressbook.add_multi(addressbook)
    assert len(multi_addressbook.multi_book) == 1

def test_delmultibook(contacts,addressbook,multi_addressbook):
    addressbook.add_person(contacts)
    multi_addressbook.add_multi(addressbook)
    assert len(multi_addressbook.multi_book) == 1
    multi_addressbook.delete_book('work')
    assert len(multi_addressbook.multi_book) == 0

def test_updatebook(contacts,addressbook,multi_addressbook,contacts1):
    addressbook.add_person(contacts)
    multi_addressbook.add_multi(addressbook)
    for v in addressbook.people.values():
        assert v.last_name == 'p'
    addressbook.update(contacts1)
    for v in addressbook.people.values():
        assert v.last_name == 'patil'

def test_employeename(contacts,addressbook):
    addressbook.add_person(contacts)
    for v in addressbook.people.values():
        assert v.first_name == 'ashish'
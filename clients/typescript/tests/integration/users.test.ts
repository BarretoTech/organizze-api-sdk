import { describe, it } from 'node:test';
import assert from 'node:assert';
import { UsersApi } from '../../index';
import { getTestConfig } from '../setup';

describe('UsersApi - Integration Tests', () => {
  it('should list users', async () => {
    const config = getTestConfig();
    const api = new UsersApi(config);

    const users = await api.listUsers();
    assert.ok(Array.isArray(users), 'should return an array');
    assert.ok(users.length > 0, 'should have at least one user');
  });

  it('should read a user by ID', async (t) => {
    const config = getTestConfig();
    const api = new UsersApi(config);

    const users = await api.listUsers();
    if (users.length === 0) {
      t.skip('No users available for testing');
      return;
    }

    const firstUser = users[0];
    const user = await api.readUser({ userID: firstUser.id });

    assert.ok(user, 'should return a user');
    assert.strictEqual(user.id, firstUser.id, 'should return the correct user');
    assert.ok(user.email, 'user should have an email');
    assert.ok(user.name, 'user should have a name');
  });
});

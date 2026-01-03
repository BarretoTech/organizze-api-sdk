import { describe, it } from 'node:test';
import assert from 'node:assert';
import { UsersApi, Configuration } from '../../index';

describe('UsersApi - Unit Tests', () => {
  it('should instantiate UsersApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new UsersApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new UsersApi(config);

    assert.ok(typeof api.listUsers === 'function', 'should have listUsers method');
    assert.ok(typeof api.readUser === 'function', 'should have readUser method');
  });
});

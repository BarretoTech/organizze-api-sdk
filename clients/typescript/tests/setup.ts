import { Configuration } from '../index';
import { config as loadDotenv } from 'dotenv';

// Load environment variables from .env file
loadDotenv();

/**
 * Get test configuration from environment variables
 * Throws an error if required environment variables are not set
 */
export function getTestConfig(): Configuration {
  const username = process.env.ORGANIZZE_EMAIL;
  const password = process.env.ORGANIZZE_API_KEY;

  if (!username || !password) {
    throw new Error(
      'ORGANIZZE_EMAIL and ORGANIZZE_API_KEY environment variables must be set for integration tests. ' +
      'Copy .env.example to .env and add your credentials.'
    );
  }

  return new Configuration({
    basePath: process.env.ORGANIZZE_BASE_URL || 'https://api.organizze.com.br/rest/v2',
    username,
    password,
    headers: {
      'User-Agent': 'organizze-api-sdk-tests (test@example.com)',
    },
  });
}

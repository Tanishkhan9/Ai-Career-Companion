import { configureStore } from '@reduxjs/toolkit';

// placeholder reducer object – add your slices here as you create them
const rootReducer = {
  // example: user: userReducer,
};

export const store = configureStore({
  reducer: rootReducer,
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

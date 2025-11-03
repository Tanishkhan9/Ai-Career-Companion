import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UserState {
  isAuthenticated: boolean;
  profile: {
    email?: string;
    name?: string;
    linkedInConnected: boolean;
  };
}

const initialState: UserState = {
  isAuthenticated: false,
  profile: {
    linkedInConnected: false,
  },
};

export const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setAuthenticated: (state, action: PayloadAction<boolean>) => {
      state.isAuthenticated = action.payload;
    },
    setProfile: (state, action: PayloadAction<Partial<UserState['profile']>>) => {
      state.profile = { ...state.profile, ...action.payload };
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.profile = initialState.profile;
    },
  },
});

export const { setAuthenticated, setProfile, logout } = userSlice.actions;
export default userSlice.reducer;
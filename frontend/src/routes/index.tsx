import { createBrowserRouter } from "react-router-dom";
import { MainLayout } from "@/layouts/MainLayout";
import { DashboardLayout } from "@/layouts/DashboardLayout";
import { ProtectedRoute } from "./ProtectedRoute";

import HomePage from "@/pages/Home/HomePage";
import LoginPage from "@/pages/Login/LoginPage";
import SignupPage from "@/pages/Signup/SignupPage";
import DashboardPage from "@/pages/Dashboard/DashboardPage";
import PythonRoadmapPage from "@/pages/Python/PythonRoadmapPage";
import LessonPage from "@/pages/Lesson/LessonPage";
import PracticePage from "@/pages/Practice/PracticePage";
import QuizPage from "@/pages/Quiz/QuizPage";
import ProfilePage from "@/pages/Profile/ProfilePage";
import NotFoundPage from "@/pages/NotFound/NotFoundPage";

import { ROUTES } from "@/utils/constants";

export const router = createBrowserRouter([
  {
    element: <MainLayout />,
    children: [
      { path: ROUTES.home, element: <HomePage /> },
      { path: ROUTES.login, element: <LoginPage /> },
      { path: ROUTES.signup, element: <SignupPage /> },
      { path: "/learn/:moduleSlug", element: <PythonRoadmapPage /> },
      { path: "/learn/:moduleSlug/lesson/:lessonSlug", element: <LessonPage /> },
      { path: "/learn/:moduleSlug/quiz/:quizId", element: <QuizPage /> },
    ],
  },
  {
    element: <ProtectedRoute />,
    children: [
      {
        element: <DashboardLayout />,
        children: [
          { path: ROUTES.dashboard, element: <DashboardPage /> },
          { path: ROUTES.profile, element: <ProfilePage /> },
        ],
      },
      // Practice runs full-bleed (own editor chrome), so it skips the dashboard shell.
      { path: "/learn/:moduleSlug/practice/:questionId", element: <PracticePage /> },
    ],
  },
  { path: "*", element: <NotFoundPage /> },
]);

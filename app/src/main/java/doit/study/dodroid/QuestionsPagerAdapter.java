package doit.study.dodroid;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;

import java.util.ArrayList;


class QuestionsPagerAdapter extends FragmentStatePagerAdapter {
    private ArrayList<Question> mQuestions;

    public QuestionsPagerAdapter(FragmentManager fm, ArrayList<Question> questions) {
        super(fm);
        this.mQuestions = questions;
    }


    @Override
    public Fragment getItem(int position) {
        return QuestionFragment.newInstance(mQuestions.get(position), getCount(), position+1);
    }


    @Override
    public int getCount() {
        return mQuestions.size();
    }


    @Override
    public CharSequence getPageTitle(int position) {
        String title = "";
        for (String tag: mQuestions.get(position).tags)
            title += tag+":";
        title += (position+1) + "/" + getCount();
        return title;
    }

}

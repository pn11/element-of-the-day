import pandas as pd
import plotly.express as px


def main():
    def atomic_number_to_symbol(number):
        return atomic_dic[number]

    def make_df(filename, label):
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Atomic Symbol'] = df['Atomic Number'].apply(
            atomic_number_to_symbol)
        df['Account'] = [label]*len(df)
        return df

    df_atomic_number = pd.read_csv("atomic_number.csv")
    atomic_dic = {n: s for n, s in zip(
        df_atomic_number['Number'], df_atomic_number['Symbol'])}

    df_nowohyeah = make_df("nowohyeah.csv", "nowohyeah")
    df_accsempai = make_df("accsempai.csv", "accsempai")

    df = pd.concat([df_accsempai, df_nowohyeah])

    fig = px.scatter(df, x='Date', y='Atomic Number',
                     text='Atomic Symbol', size_max=60, color='Account')
    fig.update_traces(textposition='top center',
                      textfont_size=24, marker={"size": 12})

    fig.update_layout(
        font=dict(
            size=24,
        )
    )

    fig.write_html("docs/plot.html")
    fig.show()


if __name__ == '__main__':
    main()
